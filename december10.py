import random

def randomlist(x):
    my_list = []
    for i in range(x):
        my_list.append(random.randint(0, 100))
    return my_list

print(randomlist(10))