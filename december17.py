import random

money = 30
keepplaying = True

def randomlist(x):
    my_list = []
    for i in range(x):
        my_list.append(random.randint(0, 100))
    return my_list

while keepplaying == True:
    print("Du har", money, "kr")
    choice = input("Vill du köpa en lott för 5kr? Ja/Nej ").lower()
    if choice == "ja" and money > 4:
        money -= 5
        winner = random.randint(0, 100)
        lotto = randomlist(7)
        for i in range(6):
            if lotto[i] == winner:
                print("Du vann 30kr!")
                money += 30
    elif choice == "ja" and money < 5:
        print("Du har inte råd")
        keepplaying = False
    else:
        keepplaying = False