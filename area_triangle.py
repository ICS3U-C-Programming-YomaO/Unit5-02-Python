#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: November, 2025
# This program calculates the area of a triangle


# function for calculating area
def calc_area(base, height):
    area = 0.5 * base * height
    print(f"The area of the triangle is {area} cm^2")


# welcome message
def main():
    print("Welcome to the area of a triangle calculator!")

    # Try catch for base
    try:
        # Ask the user for base
        base = float(input("Enter the base (cm): "))
    except ValueError:
        print("Enter a valid base!")
        return
    # stop the program
    # try catch for height
    try:
        # Ask the user for height
        height = float(input("Enter the height (cm): "))
    except ValueError:
        print("Enter a valid height!")
        return
    # stop the program

    calc_area(base, height)


main()
