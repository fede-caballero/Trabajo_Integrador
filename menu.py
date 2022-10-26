import random
from character_new import Character
from constants import *

def select_amount_character():
    while True:
        amount = int(input(CHAR_AMOU))
        if amount > 3 or amount <= 0:
            print(CHAR_AMOUN_ERR)
        else:
            return amount


def select_race():
    while True:
        print(TYPES_CHAR)
        race = int(input(CHOICE))
        if race == 0 or race < 0 or race >= 4:
            print(CHOICE_ERR)
        else:
            break
    name = str(input(CHAR_NAME))
    age = int(input(CHAR_AGE))
    print(SUM_ATTRIBS)
    sum = 0
    while sum != 15:
        strength = int(input(CHAR_STR))
        sum_1 = 15 - strength
        print(YOU_HAVE, sum_1, POINTS_LEFT)
        agi = int(input(CHAR_AGI))
        sum_1 = 15 - (strength + agi)
        print(YOU_HAVE, sum_1, POINTS_LEFT)
        con = int(input(CHAR_CONS))
        sum = strength + agi + con
        if sum == 15:
            break
        else:
            print(SUM_ERR)

    if race == 1:
        strength = strength + 2
        damage = strength // 3
        orc = Character(name, age, strength, agi, con, "orc", damage)
        return orc
    elif race == 2:
        agi = agi + 2
        damage = strength // 3
        elf = Character(name, age, strength, agi, con, "elf", damage)
        return elf
    elif race == 3:
        con = con + 2
        damage = strength // 3
        human = Character(name, age, strength, agi, con, "human", damage)
        return human


def select_character(cc):
    count = 0
    for i in cc:
        count += 1
        print(f"{count}: the name of character is {i.name} and race is {i.race}")
    while True:
        option = int(input("Which character do you want to choose: "))
        if option == 1:
            character_select = cc.pop(0)
            break
        elif option == 2 and count >= 2:
            character_select = cc.pop(1)
            break
        elif option == 3 and count == 3:
            character_select = cc.pop(2)
            break
        else:
            print("Your selection is invalid or the character does not exist")
    print(f"The selected character is: {character_select.name} and your race is: {character_select.race}")
    return character_select


def remove_character(cc):
    count = 0
    for i in cc:
        count += 1
        print(f"{count}: the name of character is {i.name} and race is {i.race}")
    while True:
        option = int(input("Choose the character you want to remove: "))
        if option == 1:
            cc.remove(cc[0])
            break
        elif option == 2 and count >= 2:
            cc.remove(cc[1])
            break
        elif option == 3 and count == 3:
            cc.remove(cc[2])
            break
        else:
            print("Your selection is invalid or the character does not exist")
    print("The character was eliminated")
    return cc


def dice():
    nums_1 = random.randint(1, 6)
    nums_2 = random.randint(1, 6)
    sum_number = nums_1 + nums_2
    return sum_number
