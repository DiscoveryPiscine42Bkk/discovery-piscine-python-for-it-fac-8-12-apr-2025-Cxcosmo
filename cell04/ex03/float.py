#!/usr/bin/env python3
def main() :
    num = float(input("Give me a number: "))
    num_float = num % 1
    if not num_float :
        print("This number is an integer.")
    else :
        print("This number is a decimal.")
main()
