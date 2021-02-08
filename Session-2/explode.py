#TASK-6.2
# * makes a iterable object into little elements of the object
def add(a,b):
    print(f'{a:,.2f} + {b:,.2f} = {a+b:>15,.2f}')

def foo(a,b):
    print(a,b)

shares = (10000.567, 10000.567)
# add(shares) -->TypeError
add(*shares)

#foo('Hi') -->TypeError 
foo(*'Hi')
