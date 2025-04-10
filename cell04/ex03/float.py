#!/usr/bin/env python3
def main() :
    num = input("Give me a number: ")
    dot_index = num.find(".")
    if dot_index == -1 :
        print("This number is an integer.")
    else :
        num_float = int(num[dot_index + 1:])
        if not num_float :
            print("This number is an integer.")
        else :
            print("This number is a decimal.")
main()
