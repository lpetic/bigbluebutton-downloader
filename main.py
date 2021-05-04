#!/usr/bin/env python3

import sys
from src.dl_presentation import dl_presentation

def main():
    if len(sys.argv) == 2 and sys.argv[1] == 'help':
        print(open('./docs/help.txt', 'r').read())
        return 0

    if len(sys.argv) < 3: 
        return -1

    if sys.argv[1] == 'presentation':
        return dl_presentation(sys.argv[2])

    return 0

if __name__ == '__main__':
    main()
