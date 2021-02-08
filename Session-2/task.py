#TASK-6.1
def calculate_product(*args):
    product = 1
    for x in args:
        product *= x
    return product

print(calculate_product(10,20,30))
print(calculate_product(*list(range(1,6,2))))