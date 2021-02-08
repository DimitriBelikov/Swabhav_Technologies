my_list = [10,20,30]
new_list = [number for number in my_list if number>=20]
print(new_list)

new_list = [number**2 if number>=20 else 0 for number in my_list]
print(new_list)