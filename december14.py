def has_equal_ends(x):
    y = -1
    for i in (x):
        y += 1
    if x[0] == x[y]:
        return True
    else:
        return False

my_list = ["Samuel", "Lucas", "Mac", "Samuel"]
print(has_equal_ends(my_list))