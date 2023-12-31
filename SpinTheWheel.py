import random

ls = []
while True:
    name = input("Enter a name: ")
    num = input("Enter a chance: ")
    if not num.isnumeric():
        print("Please enter a numeric value")
        continue
    ls.append((name, int(num)))
    cont = input("Are you done? [y/n]: ")
    if cont.lower() == 'y':
        break

wheel = []
for i in ls:
    for k in range(i[1]):
        wheel.append(i[0])

print(wheel[random.randint(0, len(wheel))])