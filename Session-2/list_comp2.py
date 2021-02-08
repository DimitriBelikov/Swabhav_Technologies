#TASK-4.3

#PART-1
print('PART-1')
from random import randint
list1 = [randint(1,5) for i in range(11)]
print(list1)

#PART-2
#Converted List Comprehension
print('\nPART-2')
list1 = [[1,2,3], [4,5,6], [7,8,9]]

results = [x 
for y in list1 
for x in y]

print(results)