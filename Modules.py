from itertools import count
import random

# abstact class
class Character:
    _ids = count(1)
    exists = True
    def __init__(self, given_name):

        self.name = given_name
        self.health = 100
        self.health_max = 100
        self.mana = 50
        self.mana_max = 50
        self.id = next(self._ids)
        self.gold = 0
        self.exp = 0
        self.exp_max = 10
        self.dmg = 15
        self.level = 1
        self.job = "Newbie"
        self.weapon = "Bare Fists!"


    def print_basic(self):
        print("Job: {0}, Level: {1}, Dmg: {2} HP: {3} / {4}, MP: {5} / {6} ".format(self.job, self.level, self.dmg,
                                                                        self.health, self.health_max,
                                                                        self.mana, self.mana_max))

    def print_weapon(self):
        print("Weapon is: " + self.weapon)

        #prints gold, exp, exp_max
    def print_gold_exp(self):
        print("Gold: {0}, Exp: {1} / {2}".format(self.gold, self.exp, self.exp_max))

        #basic attack
    def basic_attack(self, enemy):
        print("########################################")
        print("{0} is using Basic Attack! Doing {1} Dmg".format(self.name, self.dmg))
        enemy.enemy_update(self.dmg)

        #after every fight char will use this function to level up if needed
    def char_update(self, exp_gain, gold_gain): #exp / gold from the object Enemy
        if self.exp + exp_gain >= self.exp_max:
            print("Level up!")
            self.level += 1
            self.exp = 0
            self.exp_max += 6
            self.health_max += 2
            self.mana_max += 2
            self.health = self.health_max
            self.mana = self.mana_max

        else:
            self.exp += exp_gain

        self.gold = gold_gain
        self.print_basic()
        self.print_gold_exp()

    def char_hurt(self, enemy_dmg):
        self.health -= enemy_dmg
        print("{0}'s health is now: {1} / {2}".format(self.name, self.health, self.health_max))


class Warrior(Character):

    def __init__(self, given_name):
        super().__init__(given_name) # gets the properties from Character
        self.level = 3
        self.health_max = 150
        self.health = self.health_max
        self.mana_max = 50
        self.mana = self.mana_max
        self.weapon = "Basic Sword"
        self.dmg += 4
        self.job = 'Warrior'

    #a skill
    def slash(self, enemy):
        extra_dmg = 10
        mana_consume = 10
        print("Using Slash!")
        print("{0} is using the Slash skill! "
              "Doing {1} Dmg, consumes {2} mana".format(self.name, self.dmg+extra_dmg, mana_consume))
        enemy.enemy_update(self.dmg + extra_dmg)



class Mage(Character):
    def __init__(self, given_name):
        super().__init__(given_name) # gets the properties from Character
        self.level = 3
        self.health_max = 120
        self.health = self.health_max
        self.mana_max = 100
        self.mana = self.mana_max
        self.weapon = "Basic Staff"
        self.dmg += 2
        self.job = 'Mage'

    #A skill
    def fire_blast(self, enemy):
        extra_dmg = 14
        mana_consume = 20
        print("Using Fire Blast!")
        print("{0} is using the Fire Blast skill! "
              "Doing {1} Dmg, consumes {2} mana".format(self.name, self.dmg+extra_dmg, mana_consume))
        enemy.enemy_update(self.dmg+extra_dmg)


class Enemy(Character):

    def __init__(self, char_level):
        super().__init__(char_level)
        self.name = self.random_name()
        self.level = char_level
        self.health_max = 40 + char_level * 5
        self.mana_max = 40 + char_level * 2
        self.health = self.health_max
        self.mana = self.mana_max
        self.exp_gain = char_level*5
        self.gold_gain = char_level*3
        self.dmg = char_level*3



    def print_all(self):
        print("##############################")
        print("You have encountered an enemy!")
        print("Name: {0}, Level: {1}, HP: {2} / {3}, MP: {4} / {5}, Dmg: {6}".format(self.name, self.level,
                                                                                     self.health, self.health_max,
                                                                                     self.mana, self.mana_max,
                                                                                     self.dmg))

    # returns a random name from the list, string type
    def random_name(self):
        monster_names = ['Gremlin', 'Davy Jones', 'Flamewoman', 'Guttaur', 'Grimetalon', 'Grimetalon', 'Blightwings',
                         'Blightwings', 'The Wild Shrieker', 'The Bronze Behemoth']
                                #10 names 0 - 9
        rand_name = random.choice(monster_names)
        return rand_name


    # when enemy attacks me
    def enemy_attack(self, player):
        print("MUHAAAAAA!")
        player.char_hurt(self.dmg)


    #when enemy is under attack
    def enemy_update(self, player_dmg):
        self.health -= player_dmg
        print("Enemy's health is now: {0} / {1}".format(self.health, self.health_max))


class Item:
    def __init__(self, item_name, level, dmg_boost, price, weaptype):
        self.name = item_name
        self.level = level
        self.dmg_boost = dmg_boost
        self.price = price
        self.weaptype = weaptype #Sword / Staff...

    def print_item_stats(self):
        print("Item Properties: Name: {0}, Level: {1}, Price {2}, Dmg {3}, Type: {4}".format(self.name, self.level,
                                                                            self.price, self.dmg_boost,
                                                                            self.weaptype))
