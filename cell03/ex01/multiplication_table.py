#!/usr/bin/env python3
def main() :
    start = 0
    print("Enter a number")
    num = int(input())
    while start <= 9 :
        print(f"{start} x {num} = {start * num}")
        start += 1
main()
