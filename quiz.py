# What will be the output of the following Python code?

list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]

sum = 0

sum1 = 0

for elem in list1:

if (elem % 2 == 0):
sum = sum + elem
if (elem % 3 == 0):

sum1 = sum1 + elem

print(sum , end=" ")