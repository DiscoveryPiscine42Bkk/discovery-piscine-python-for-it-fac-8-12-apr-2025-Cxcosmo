#!/usr/bin/env python3
import sys
def main() :
    if len(sys.argv) > 1 :
        print("none")
    else :
        i = 0
        while i <= 10 :
            j = 0
            list_num = []
            while j <= 10 :
                list_num.append(str(i * j))
                j += 1
            print(f"Table de {i} : {" ".join(list_num)}")
            i += 1
main()
