def update(k):
    print('Id of K Before = ', id(k))
    k = 0
    print('Id of K After = ', id(k))

x = 10
update(x)
print(x)
