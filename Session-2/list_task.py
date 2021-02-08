#TASK-3
rainbow = ['green', 'orange', 'violet']

index_violet = rainbow.index('violet')
print(index_violet)
rainbow[index_violet:index_violet] = ['red']
print(rainbow)

rainbow.append('yellow')
print(rainbow)

rainbow1 = rainbow[::-1]
print(rainbow1)

rainbow.remove('orange')
print(rainbow)