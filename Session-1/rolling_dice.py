from random import randint

face_count = {}
for i in range(1,7):
    face_count[str(i)] = 0

for x in range(1,100):
    rand_int = randint(1,6)
    face_count[str(rand_int)] += 1

print(face_count)