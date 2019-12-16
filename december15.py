def is_palindrom(x):
    pal = x[::-1]
    if x == pal:
        return True
    else:
        return False

print(is_palindrom("anna"))