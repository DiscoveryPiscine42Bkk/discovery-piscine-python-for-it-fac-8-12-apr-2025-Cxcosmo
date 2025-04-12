#!/usr/bin/env python3
import sys, re
def main() :
    count_same = 0 
    if len(sys.argv) - 1 == 2 :
        count_same = len(re.findall(sys.argv[1], sys.argv[2]))
    print(count_same if count_same else "none")
main()
