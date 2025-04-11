from checkmate import checkmate
import sys
def main():
    files = sys.argv
    if len(files) == 1 :
        print("Need some file.chess")
    else :
        for i in files :
            if i.find(".chess") != -1 :
                with open(i, 'r') as files_chess :
                    board = files_chess.read()
                checkmate(board)

if __name__ == "__main__" :
    main()
