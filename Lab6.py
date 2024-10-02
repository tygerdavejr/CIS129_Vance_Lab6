# Module 6 Lab
# David Vance
# Professor Kevin Chang
# CIS 129 - Programming and Problem Solving 1

"""
Hot Dog Cookout Calculator

Assume that hot dogs come in packages of 10, and hot dog buns come in packages
of 8.  Design a modular program that calculates the number of packages of hot 
dogs and the number of packages of hot dog buns needed for a cookout, with the
minimum amount of leftovers.

The program should ask the user for the number of people attending the cookout,
and the number of hot dogs each person will be given. 

The program should display the following:
    1. The minimum number of packages of hot dogs required.
    2. The minimum number of packages of buns required
    3. The number of hot dogs that will be left over
    4. The number of buns that will be left over
"""

# INITIALIZING
# Import libraries, define functions and set variables as needed

import math  # This is necessary to call the math.ceil function below


def main():
    """Get the number of hotdogs needed, then calculate values for leftover and
    minimum needed hotdogs, then calculate values for leftover and minimum 

    
            needed buns"""

    # Get the total number of hot dogs needed
    total = get_total_hot_dogs()

    # Named Constants
    dogs_per_package = 10  # The number of hot dogs in a package
    buns_per_package = 8   # The number of buns in a package

    # Local variables
    # I don't believe this is necessary; I've run the program without just
    # fine. However, I am including it because it was in the assignment's
    # pseudocode.
    dogs_left = 0
    buns_left = 0
    min_dogs = 0
    min_buns = 0

    # Calculate for leftover and minimum hot dogs
    dogs_left = (dogs_per_package - total % dogs_per_package) % dogs_per_package
    min_dogs = math.ceil(total / dogs_per_package) 

    # Calculate for leftover and minimum buns
    buns_left = (buns_per_package - total % buns_per_package) % buns_per_package
    min_buns = math.ceil(total / buns_per_package) 

    # Display results
    show_results(dogs_left, min_dogs, buns_left, min_buns)
    return


def get_total_hot_dogs():
    """This module gets the number of people attending the cookout, the 
    number of hot dogs each person will be given, calculates the total hot
    dogs needed, and stores the result in the total_hot_dogs reference
    variable."""
    
    # Get the number of people attending and hotdogs per
    people = int(input('Enter the number of people attending the cookout:')) 
    hot_dogs_per = int(input('Enter the number of hot dogs for each person: '))

    # Calculate the total number of hotdogs needed
    total_hot_dogs = people * hot_dogs_per
    return total_hot_dogs


def show_results(dogs_left, min_dogs, buns_left, min_buns):
    """This module receives the total number of hot dogs
    as an argument and calculates the minimum packages of hot
    dogs and hot dog buns, the left over hot dogs and hot dog
    buns, and displays the results."""
    # This description from the pseudocode is incorrect.  This module
    # accepts the values calculated in main() and displays the result.

    # Display the minimum packages of hotdogs and buns needed
    print('Minimum packages of hot dogs needed: ', min_dogs)
    print('Minimum packages of hot dog buns needed: ', min_buns)

    # Display the number of hot dogs and buns left over
    print('Hot dogs left over: ', dogs_left)
    print('Hot dog buns left over: ', buns_left)
    return

# PROCESSING
# With all libraries imported, functions defined and variables assigned it is
# time to actually initialize the program.

main() 


# TERMINATION
# The outputs are actually given in the show_results module.
