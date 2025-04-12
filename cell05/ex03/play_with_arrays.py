#!/usr/bin/env python3
import json
def main() :
    original_list = json.loads(input())
    new_list = []
    for i in original_list :
        if i > 5 :
            new_list.append(i + 2)
    print(set(new_list)) 
main()
