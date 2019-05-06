import random

difficulty_mode = int(input("1 - easy, 2 - difficult and 3 - Very difficult. Enter game mode (1/2/3)? "))

health = 50

difficulty = difficulty_mode

portion_health = int(random.randint(25,50) / difficulty)

health = health + portion_health

print ("The health is ",health)