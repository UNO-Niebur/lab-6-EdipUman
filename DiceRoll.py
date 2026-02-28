#DiceRoll.py
#Name:Edip Uma
#Date:02/28/26
#Assignment:Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range (10000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
  #find the sum total of the two dice
    diceSum = dice1 + dice2
    rolls[diceSum - 2] = rolls[diceSum -2] + 1
  #print statictics for dice rolls
  dice = 2
  for count in rolls:
    percent = (count / 10000) * 100
    print(dice, ":", count, "=", round(percent, 2), "% of total rolls")
    dice = dice + 1

if __name__ == '__main__':
  main()
