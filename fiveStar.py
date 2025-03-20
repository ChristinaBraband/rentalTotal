"""
Chapter 2 Programming Exercise
(Page 50)
Program: fiveStar.py
2/24/2025

Simple app that prompts the user for the total number of rentals in different price categories.
Calculates and displays the grand total.
"""

# Variables / Constants / Objects

NEW_VIDEOS = 3.0
OLD_VIDEOS = 2.0

#Input phase
numNew = int(input("Please, enter the amount of new videos rented: "))
numOld = int(input("Next, enter the amount of old videos:  "))

#Processing phase
grandTotal = (NEW_VIDEOS * numNew) + (OLD_VIDEOS * numOld)

print("\nThe total charge is $ " + str(round(grandTotal, 2))) 
input("Press ENTER to exit the program...")