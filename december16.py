import random

def randomlist(x):
    my_list = []
    for i in range(x):
        my_list.append(random.randint(0, 100))
    return my_list

winner = random.randint(0, 100)
lotto = randomlist(7)
print(lotto)
print(winner)

for i in range(6):
    if lotto[i] == winner:
        print("Du vann!")