import random
from character_new import Character


def select_amount_character():
    while True:
        amount = int(input("How many characters do you want to add(max 3): "))
        if amount > 3 or amount <= 0:
            print("Only 3 characters maximum allowed and it can't be 0")
        else:
            return amount


def select_race():
    while True:
        print(
            "Enter the type of character you want to choose:\n "
            " 1:Orc: You'll get 2 extra points in strength\n "
            " 2:Elf: You'll get 2 extra points in agility\n "
            " 3:Human: You'll get 2 extra points in constitution ")
        race = int(input("your option: "))
        if race == 0 or race < 0 or race >= 4:
            print("your option is not in the options")
        else:
            break
    name = str(input("Enter character name: "))
    age = int(input("Enter character age:"))
    print("the sum of strength, life and agility must give 15 and none can be worth 0")
    sum = 0
    while sum != 15:
        strength = int(input("Enter character strength :"))
        sum_1 = 15 - strength
        print("you have", sum_1, "available values left")
        agi = int(input("Enter character agi :"))
        sum_1 = 15 - (strength + agi)
        print("you have", sum_1, "available values left")
        con = int(input("Enter character con:"))
        sum = strength + agi + con
        if sum == 15:
            break
        else:
            print("THE SUM OF THE VALUES IS NOT 15, ENTER THE VALUES AGAIN")

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
