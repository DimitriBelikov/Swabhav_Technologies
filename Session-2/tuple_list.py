#TASK-2

#PART - 1
print('\nPART-1')
t1 = (10,20)
print(id(t1))
t1 += (3,4)
print(id(t1))
print(t1)


#PART-2
print('\nPART-2')
list1 = [10,20]
print(id(list1))
list1 += (30,40)
list1 += "Hello"
print(id(list1))
print(list1)

#PART-3
print('\nPART-3')
student_tuple = ('susha', [10,20,30])
print(student_tuple[1][0])
student_tuple[1][0] = 100
print(student_tuple)
