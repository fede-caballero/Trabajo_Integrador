import random
from character_new import Character
from constants import *


def select_amount_character():
    
    while True:
        try:
            amount = int(input(CHAR_AMOUNT))
            if amount > 3 or amount <= 0:
                print(CHAR_AMOUNT_ERR)
            else:
                return amount
        except:
            pass
    
    
def select_race():
    while True:
        try:
            print(CHOICE_TYPES_CHAR)
            race = int(input(YOUR_CHOICE))
            if race == 0 or race < 0 or race >= 4:
                print(CHAR_CHOICE_ERROR)
            else:
                break
        except:
            pass

    while True:
        try:
            name = str(input(CHAR_NAME))
            age = int(input(CHAR_AGE))
            break
        except:
            pass

    print(SUM_ATTRIBS)

    while True:
        try:
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

        except:
            pass

    if race == 1:
        strength = strength + 2
        damage = strength // 3
        orc = Character(name, age, strength, agi, con, "Orc", damage)
        return orc
    elif race == 2:
        agi = agi + 2
        damage = strength // 3
        elf = Character(name, age, strength, agi, con, "Elf", damage)
        return elf
    elif race == 3:
        con = con + 2
        damage = strength // 3
        human = Character(name, age, strength, agi, con, "Human", damage)
        return human


def select_character(cc):
    count = 0
    for i in cc:
        count += 1
        print(f"{count}",NAME_OF_CHAR,f"{i.name}", RACE_IS, f"{i.race}")
    while True:
        option = int(input(CHAR_TO_CHOOSE))
        if option == 1:
            character_selected = cc.pop(0)
            break
        elif option == 2 and count >= 2:
            character_selected = cc.pop(1)
            break
        elif option == 3 and count == 3:
            character_selected = cc.pop(2)
            break
        else:
            print(INVALID_SELECTION)
    print(SELECTED_CHAR, f"{character_selected.name}",RACE_IS, f"{character_selected.race}")
    return character_selected


def remove_character(cc):
    count = 0
    for i in cc:
        count += 1
        print(f"{count}",NAME_OF_CHAR,f"{i.name}", RACE_IS, f"{i.race}")
    while True:
        option = int(input(CHAR_TO_REMOVE))
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
            print(INVALID_SELECTION)
    print(CHAR_REMOVED)
    return cc


def dice():
    nums_1 = random.randint(1, 6)
    nums_2 = random.randint(1, 6)
    sum_number = nums_1 + nums_2
    return sum_number


def check_inventory(inventory):
    print(INVENTORY)
    count = 1
    for i in inventory:
        print(f"{count}", POTION, f"{i.name}", f"{i.con}", HEALTH_POINTS)
        count += 1

    option_selected = int(input(POTION_SELECT))
    return option_selected - 1
