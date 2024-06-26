import json

# Load JSON data into dictionary
with open('data.json') as file:
 
    data = json.load(file)
def get_definition(word):
    return data.get(word.lower(), "Word not found in dictionary")

def suggest_word(word):
    closest_matches = difflib.get_close_matches(word, data.keys())

# Test the functions
word = input("Enter a word: ")
definition = get_definition(word)
if definition == "Word not found in dictionary":
    print("Word not found in dictionary.")
    suggestion = suggest_word(word)
    if suggestion:
        print("Did you mean:", suggestion[0])
else:
    print("Definition:", definition)
