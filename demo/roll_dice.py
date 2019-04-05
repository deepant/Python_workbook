import random
class Dice:


    def roll (self):
        first = random.randint (1 , 6)
        second = random.randint (1 , 6)
        return first, second
#def roll ():
 #   number_tupple = {1, 2, 3, 4, 5, 6}
  #  return random.randrange(number_tupple)

#ran_d = roll()
#print(ran_d)

dice = Dice()
print(dice.roll())
print(dice.roll())
print(dice.roll())
print(dice.roll())
print(dice.roll())
print(dice.roll())
print(dice.roll())
print(dice.roll())
print(dice.roll())
