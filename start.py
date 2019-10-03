from Modules import *
import time
import sys
import random

'''
modified a few things:
Game is ending at lvl 7.
Added a shop with 2 items.
Added job advance.

Will continue with other projects that includes graphics, like Unity.
'''
#initilize weapon list: static weapon list
WEAP_LIST = []
sword = Item("Wicked Longsword", 3, 10, 1, 'Warrior')
staff = Item("Arcane Grand Staff", 3, 10, 1, 'Mage')
WEAP_LIST.append(sword)
WEAP_LIST.append(staff)

#print styles
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.3)

def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def print_med(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def main():
    print("####################################")
    print_med("Welcome to the Eden's RPG text game\n")
    print("####################################\n")
    print_fast("#            - Play -              #\n")
    print_fast("#            - Help -              #\n")
    print_fast("#            - Quit -              #\n")
    print("####################################\n")
    print_med('Enter your decision: \n')
    decision = input()

    while decision.lower() != 'play' and decision.lower() != 'help' and decision.lower() != 'quit':
        decision = input("Invalid decision, enter your decision: ")

    if decision.lower() == 'play':
        game_loop()
    elif decision.lower() == 'help':
        help_section_title()
    elif decision.lower() == 'quit':
        print_med("Exit in 2 seconds\n")
        time.sleep(2)
        quit()

def fight(player, enemy):
    print("|             ------------                  |")
    print("|             FIGHT STARTED                 |")
    print("|             ------------                  |")
    while True:
        print_fast("{0} Turn!\n".format(player.name))
        player_turn(player, enemy)
        if not check_alive(enemy):
            print("You have killed {0}!".format(enemy.name))
            player.char_update(enemy.exp_gain, enemy.gold_gain)
            del enemy
            break
        print("#########")
        print("{0} Turn!".format(enemy.name))
        enemy_turn(player, enemy)
        if not check_alive(player):
            print("The player died!")
            print("Unfortunately you lost, leaving game in 3 seconds. ")
            time.sleep(3)
            quit()

    break_section(player)




def player_decision(player):
    print_med("Commands: Combat \n")
    decision = input()

    while decision.lower() != 'combat':
        decision = input("Invalid, enter your decision: ")



    if decision.lower() == 'combat':
        if type(player) is Character:
            print_fast("Choose your attack: Basic Attack, return: ")
            decision = input()
        elif type(player) is Warrior:
            print_fast("Choose your attack: Basic Attack, Slash, return: ")
            decision = input()
        elif type(player) is Mage:
            print_fast("Choose your attack: Basic Attack, Fire Blast, return: ")
            decision = input()

        while decision.lower() != 'basic attack' and decision.lower() != 'return' \
                and decision.lower() != 'slash' and decision.lower() != 'fire blast':
                decision = input("Invalid, enter your decision:")

    return decision

def player_turn(player, enemy):

    decision = player_decision(player)

    if decision.lower() == 'basic attack':
        player.basic_attack(enemy)

    if decision.lower() == 'return':
        player_turn(player, enemy)

    if decision.lower() == 'slash' and type(player) is Warrior:
        player.slash(enemy)
    elif decision.lower() == 'slash' and type(player) is Character:
        print("You can't perform this combat")
        player_turn(player, enemy)

    if decision.lower() == 'fire blast' and type(player) is Mage:
        player.fire_blast(enemy)
    elif decision.lower() == 'fire blast' and type(player) is Character:
        print("You can't perform this combat")
        player_turn(player, enemy)

def check_alive(character):
    if character.health <= 0:
        return False

    return True

def enemy_turn(player, enemy):
    #  in the future, will random stuff like random skills / attacks...
    #  60% for basic attack, 40% for skills...
    print_fast("{0}'s is using Basic Attack! Doing {1} Dmg\n".format(enemy.name, enemy.dmg))
    player.char_hurt(enemy.dmg)

def game_loop():

    print("|             GAME STARTED                  |")
    print("|             ------------                  |")
    print_fast("Hello there! enter your name: \n")
    player_name = input()
    player = Character(player_name.capitalize())

    Character.exists = True # help section - in case there are no players when write stats
    print("####################################")
    print_med("Greetings {0}, your stats are: \n".format(player.name.capitalize()))
    player.print_basic()
    player.print_weapon()
    player.print_gold_exp()

    print("####################################")
    print_med("Game is simple: \n")
    print_fast("    *You are going to fight against enemies, your goal is to defeat them\n")
    print_fast("    *You can improve yourself by leveling up\n")
    print_fast("    *Unlock Job Advance at level 3 (Warrior / Mage)\n")
    print_fast("    *Unlock SHOP at level 5\n")
    print_fast("    *You can enter 'help' through the Rest Room in order to get to the Help Section\n")
    print_fast("    *Game is over once you reach to level 7.\n")
    print_slow("Good luck !\n")
    print("####################################")
    break_section(player)


def job_advance(player):

    print("------------------------------------")
    print_fast("You can now perform a job advance\n")
    print_fast("    *Warrior - Have the Slash skill, doing {0} extra dmg, and consumes {1} mana\n".format(10, 10))
    print_fast("    *Mage - Have the Fire Blast skill, doing {0} extra dmg, and consumes {1} mana\n".format(14, 20))
    print_fast("Enter your decision: Warrior, Mage: \n")
    job = input()

    while job.lower() != 'warrior' and job.lower() != 'mage':
        job = input("Invalid choice, enter again: ")

    if job.lower() == 'warrior':
        player = Warrior(player.name)
        print_slow("- You are now a Warrior! -\n")
    elif job.lower() == 'mage':
        player = Mage(player.name)
        print_slow("- You are now a Mage! -\n")

    return player

def break_section(player):


    #job advance
    if player.level == 3 and player.job == "Newbie":
        player = job_advance(player)

    #shop
    if player.level == 5:
        print("---------------------------")
        print_fast("You have unlocked the Shop\n")
        print_fast("you can buy weapons depends on your class.\n")
        print_fast("To get into the shop, use the command 'shop' at the Rest Time..\n")

    #game - finished
    if player.level == 7:
        print_fast("Well done! you have finished the game!\n")
        print_fast("Exit in 5 seconds.")
        time.sleep(5)
        quit()


    print("---------")
    print("Rest Time")
    print("---------")
    while(True):
        print_fast("What would you like to do now?\n")
        print_fast("stats, shop, skills, continue: \n")
        decision = input()
        while decision.lower() != 'stats' and \
                decision.lower() != 'shop' and \
                decision.lower() != 'skills' and\
                decision.lower() != 'continue' and\
                decision.lower() != 'help':

            decision = input("Invalid decision, enter a decision: ")

        if decision.lower() == 'help':
            help_section()

        if decision.lower() == 'stats':
            player.print_basic()
            player.print_gold_exp()
        if decision.lower() == 'shop':
            if player.level <= 4:
                print_fast("You need to reach level 5 in order to unlock SHOP, current level: {0}\n".format(player.level))
            else:
                shop(WEAP_LIST, player) #TEST NOW IF WORKS, ADDED THE OBJECT PLAYER, YOU CAN DO HIM STATIC!
        if decision.lower() == 'skills':
            if type(player) is Character: # checks if my player is character type or other types
                print_med("*You got a basic attack!\n")
            elif type(player) is Warrior:
                print_med("*You got a Basic Attack!\n")
                print_med("*You got a Slash attack!\n")
            elif type(player) is Mage:
                print_med("*You got a Basic Attack!\n")
                print_med("*You got a Fire Blast attack!\n")

        if decision.lower() == 'continue':
            enemy = Enemy(player.level)
            enemy.print_all()
            fight(player, enemy) # fight stage

def shop(WEAP_LIST, player):
    leave_shop = False
    print("####################################")
    print_fast("- Welcome to the SHOP -\n")
    print_fast("Commands: buy, leave\n")
    decision = input()
    
    while decision.lower() != 'buy' and decision.lower() != 'leave':
        decision = input("Invalid decision, enter a decision: ")

    if decision == 'buy':
        print("There are currently {0} weapons on sale: ".format(str(len(WEAP_LIST))))
        for weap in WEAP_LIST: #run through the static WEAP_LIST
            print(weap.print_item_stats())

        print_fast("Commands: sword, staff, return\n")
        while decision.lower() != 'sword' and decision.lower() != 'staff' and decision.lower() != 'return':
            decision = input("Invalid decision, enter a decision: ")

        if decision == 'sword':
            if player.job != 'Warrior':
                print("You can't use a sword since you are a Mage")
                leave_shop = True

            elif player.gold < weap.price:
                print("YOU DONT HAVE ENOUGH MONEY IN ORDER TO BUY IT.")
                leave_shop = True
            else:
                weap = WEAP_LIST.pop(1)
                player.weapon = weap
                print_fast("You have bought the Sword!\n")

        elif decision == 'staff':
            if player.job != 'Mage':
                print("You can't use a staff since you are a Warrior")
                leave_shop = True

            elif player.gold < weap.price:
                print("YOU DONT HAVE ENOUGH MONEY IN ORDER TO BUY IT.")
                leave_shop = True
            else:
                weap = WEAP_LIST.pop(1)
                player.weapon = weap
                print_fast("You have bought the Staff!\n")

    elif decision == 'leave' or leave_shop:
        return

def help_section_title():
    print("####################################")
    print("Welcome to the Help Section!")
    print("commands are: ")
    print("stats - show all stats of your character!")
    print("shop - can buy stuff from the store, only at the Rest Time")
    print("skills - show up your skills!")
    print("resume - gets back to the game")
    print("####################################")
    help_section()

def help_section():
    # test if works fine even if I don't have a hero - global player is only for not having error with player
    global player
    print_med("Choose your decision: ")
    help_dec = input()
    while help_dec.lower() != 'stats' \
            and help_dec.lower() != 'shop' \
            and help_dec.lower() != 'skills' \
            and help_dec.lower() != 'resume':
        help_dec = input("Invalid decision, Choose your decision: ")

    if help_dec.lower() == 'stats':
        if not Character.exists: #there are no players so far...
            print("You don't have a hero")
            help_section()
        else:
            try:
                player.print_basic()
                player.print_gold_exp()
                help_section()
            except BaseException:
                print("You didn't create a character")
                help_section()

    if help_dec.lower() == 'shop':
        print("Can only be opened after a fight, in the Rest Room")
        help_section()
    if help_dec.lower() == 'skills':
        print("SHOW UP THE SKILLS METHODS")
        help_section()
    if help_dec.lower() == 'resume':
        game_loop() # leaves the help_section method or fight...



if __name__ == "__main__":
    main()
    time.sleep(10)
