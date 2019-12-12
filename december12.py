def divisible_by(x, y):
    my_list = []
    for i in range(1000):
        if (i + 1) % x == 0 and (i + 1) % y != 0:
            my_list.append(i + 1)
    return my_list

print(divisible_by(7, 2))