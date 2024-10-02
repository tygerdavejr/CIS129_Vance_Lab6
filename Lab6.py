# Module 6 Lab
# David Vance
# Professor Kevin Chang
# CIS 129 - Programming and Problem Solving 1

"""
Hot Dog Cookout Calculator

Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8. 
Design a modular program that calculates the number of packages of hot dogs and the number of 
packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. 
The program should ask the user for the number of people attending the cookout, and the 
number of hot dogs each person will be given. The program should display the following:

1. The minimum number of packages of hot dogs required.
2. The minimum number of packages of buns required
3. The number of hot dogs that will be left over
4. The number of buns that will be left over
"""

# INITIALIZING
# Import libraries, define functions and set variables as needed

import math  # This is necessary to call the math.ceil function below

def get_total_hotdogs():
    """This module gets the number of people attending the cookout and the 
    number of hot dogs each person will be given, and stores the product in
    the total_hotdogs reference variable."""
    
    # Get the number of people attending the cookout
    people = int(input('Enter the number of people attending the cookout:')) 

    # Get the number of hot dogs each person will be given
    hot_dogs_per = int(input('Enter the number of hot dogs for each person: '))

    # Calculate the total number of hotdogs needed
    total_hotdogs = people * hot_dogs_per
    return total_hotdogs


def show_results(dogs_left, min_dogs, buns_left, min_buns):
    """This module accepts the total number of hot dogs as an argument and calculates the minimum packages of hot
    dogs and hot dog buns, the left over hot dogs and hot dog buns, and displays the results."""

    # Display the minimum packages of hot dogs needed
    print('Minimum packages of hot dogs needed: ', min_dogs)

    # Display the minimum packages of buns needed
    print('Minimum packages of hot dog buns needed: ', min_buns)

    # Display the number of hot dogs left over
    print('Hot dogs left over: ', dogs_left)

    # Display the number of hot dog buns left over
    print('Hot dog buns left over: ', buns_left)
    return


# Set the number of hotdogs and buns per package
dogs_per_package = 10
buns_per_package = 8

# PROCESSING
# Get the number of hotdogs needed, then calculate values for leftover and 
# minimum needed hotdogs, then calculate values for leftover and minimum
# needed buns

# Get the total number of hot dogs needed
total = get_total_hotdogs()

# Calculate the number of leftover hot dogs
dogs_left = (dogs_per_package - total % dogs_per_package) % dogs_per_package

# Calculate the minimum number of packages of hot dogs
min_dogs = math.ceil(total / dogs_per_package) 

# Calculate the number of leftover hot dog buns
buns_left = (buns_per_package - total % buns_per_package) % buns_per_package

#Calculate the minimum number of packages of hot dogs buns
min_buns = math.ceil(total / buns_per_package) 


# TERMINATION
# Display the results of hotdogs left, minimum number of hotdogs needed,
# and buns left and minimum buns needed

show_results(dogs_left, min_dogs, buns_left, min_buns)




