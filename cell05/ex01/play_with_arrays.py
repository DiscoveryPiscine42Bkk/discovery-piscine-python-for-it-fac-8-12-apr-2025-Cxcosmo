#!/usr/bin/env python3
import json
def main() :
    original_list = json.loads(input("Original array: "))
    new_list = []
    for i in original_list :
        new_list.append(i + 2)
    print(f"New array: {new_list}") 
main()

