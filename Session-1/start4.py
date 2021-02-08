x = 5
y = x

print(id(x))
print(id(x) == id(y))

x = x+5
print(id(x))