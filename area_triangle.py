#!/usr/bin/env python3
# Created By: sarah OUAMOU
# Date: 12 11 2025
# This program calculates the area of a triangle given its base and height.


def area_of_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)


def main():
    area_of_triangle()


if __name__ == "__main__":
    main()
