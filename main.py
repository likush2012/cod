import random


def hang_man():
    personages = [
        "   ------------------- \n   |                 |\n   0                 |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n   |                 |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n  /|                 |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n  /|\                |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n  /|\                |\n  /                  |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n  /|\                |\n  / \                |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________"
        ]

    words = ["stendoff 2", "stumble guys", "roblox", "fifa", "brawl stars", "among us", "pubg", "fortnite", "gta"]

    word = random.choice(words).lower()

    print("_ " * len(word))

    count = 6

    true_count = 0

    j = 0

    while count > 0:
        if true_count == len(word):
            break

        q = 0
        letter = input()

        if letter in word:
            for i in range(len(word)):
                count_letter = 0
                if letter == word[i]:
                    count_letter += 1
                    true_count += count_letter

                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print()
        else:
            print(personages[j])
            j += 1
            count -= 1

    print()
    print("----------------------------------------")
    if (count == 0):
        print("ԴՈՒՔ ՊԱՐՏՎԵՑԻՔ")
        print("ԲԱՌՆ ԷՐ ", word)
    else:
        print("ԴՈՒՔ ՀԱՂԹԵՑԻՔ")


print("ԽԱՂԻ ԿԱՆՈՆՆԵՐԸ")
print()
print("Համակարգիչը հիշողության մեջ պահում է մեքենայի անուն, անհրաժեշտ է գուշակել անունը, հերթով ներմուծելով տառերը")
print("Ճիշտ գուշակած տառի դեպքում էկրանին կհայտնվի անվան մեջ տառի դիրքը")
print("Սխալ գուշակած տառի դեպքում էկրանին կհայտնվի կախաղանը, մարդուկի մարմնի հատվածներով")
print("Խաղը կտևի այնքան, քանի դեռ ճիշտ չենք գուշակել բառը կամ մարդուկը ամբողջությամբ չի հայտնվել կախաղանի վրա")
print()
print("Դե սկսենք խաղը ::::::::::::::::::::::::::::::::::::::")

print()

hang_man()