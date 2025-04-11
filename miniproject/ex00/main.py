from checkmate import checkmate
import sys
def main():
    files = sys.argv
    for i in files :
        if i.find(".chess") != -1 :
            with open(i, 'r') as files :
                board = files.read()
            checkmate(board)

if __name__ == "__main__":
    main()
