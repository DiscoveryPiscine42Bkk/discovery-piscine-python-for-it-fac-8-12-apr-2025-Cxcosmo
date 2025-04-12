#!/usr/bin/env python3
import sys
def main() :
    print(sys.argv[1].lower() if len(sys.argv) == 2 else "none")
main()
