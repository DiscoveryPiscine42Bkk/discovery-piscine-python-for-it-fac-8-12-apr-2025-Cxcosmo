#!/usr/bin/env python3
import sys
def main() :
    if len(sys.argv) - 1 >= 2 :
        list_p = sys.argv[1:]
        for i in reversed(list_p) :
            print(i)
    else :
        print("none")
main()
