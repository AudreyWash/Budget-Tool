#!/bin/python3

from Apples import Apples

low = Apples("Red Apples", 20)
medium = Apples("Green Apples", 40)
high = Apples("Purple Apples", 60)

try:
    appleBudget = float((input("What is your apple budget?")))
except ValueError:
    exit("Please enter a number.")
    
for apples in[high, medium, low]:
    apples.buy(appleBudget)
