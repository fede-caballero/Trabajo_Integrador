from constants import *
from menu import select_amount_character, select_race, select_character, remove_character, dice
from enemy_new import * 
from login import login, crear_cuenta, comprobar_datos

enemy_control = [
    Enemy("Grom", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("Thrum", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("Doomhammer", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("Skullsplitter", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("Gorrum", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("Nagrand", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("Lok amon", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("Grombolar", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("Grommash", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("Dae'mon", 16, 7, 3, 50, "orc", 2, 100, 400)
]
character_control = []
character_selected_for_combat = ''
print("\033[;36m" + "")
"""#ingresar o crear cuenta
while True:
    print("1:Crear cuenta: \n2:Ingresar a su cuenta:")
    option = int(input("your option: "))
    if option == 1:
        crear_cuenta()
        break
    elif option == 2:
        while True:
            datos_ingresados = login()
            datos= comprobar_datos(datos_ingresados, crear_cuenta())
            if datos == True:
                break
        break
    else:
        print("su opcion no existe, ingresela nuevamente\n")"""
# cantidad de personajes
amount = select_amount_character()

# seleccion de raza
count = 0
while count != amount:
    character = select_race()
    character_control.append(character)
    count += 1

while True:
    print(MENU_OPTION)
    option = int(input(CHOICE))
    if option == 1:
        character_selected_for_combat = select_character(character_control)
        break
    elif option == 2:
        remove_character(character_control)
    elif option == 3:
        break
    else:
        print(WRONG)
        
character_turn = True
enemy = enemy_control.pop(0)
while True:
    input(FIGHT)
    dice_random = dice()
    if character_turn:
        damage_character = character_selected_for_combat.damage_send(dice_random)
        enemy.damage_received(damage_character)
        print(DAMAGE_CAUSED, f"{character_selected_for_combat.name} -----> {damage_character}", HEALTH_POINTS)
        print(CURRENT_HEALTH,f"{enemy.name}:", enemy.con, HEALTH_POINTS)
        character_turn = False

        if enemy.dead:
            print(f"{enemy.name}",DEAD)
            exp_earn = enemy.give_exp()
            character_selected_for_combat.exp = exp_earn / (len(character_control) + 1)
            character_selected_for_combat.check_to_next_level()
            if len(character_control) >= 1:
                exp_earn /= len(character_control) + 1
                for i in character_control:
                    i.exp += exp_earn
                    i.check_to_next_level()
            if len(enemy_control) >= 1:
                enemy = enemy_control.pop(0)
            else:
                break

    else:
        damage_enemy = enemy.damage_send(dice_random)
        character_selected_for_combat.damage_received(damage_enemy)
        if character_selected_for_combat.dead:
            print(f"{character_selected_for_combat.name}", DEAD)
            if len(character_control) > 0:
                character_selected_for_combat = select_character(character_control)
            else:
                break

        print(DAMAGE_CAUSED, f"{enemy.name} -----> {damage_enemy}", HEALTH_POINTS)
        print(CURRENT_HEALTH, f"{character_selected_for_combat.name}:", character_selected_for_combat.con, HEALTH_POINTS)
        character_turn = True