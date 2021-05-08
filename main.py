#!/usr/bin/env python3

import sys
from src.presentation import presentation
from src.playback import playback

def main():
    if len(sys.argv) == 1 or sys.argv[1] == 'help':
        print(open('./docs/help.txt', 'r').read())
        return 0

    if sys.argv[1] == 'presentation' and len(sys.argv) == 3:
        return presentation(sys.argv[2])

    if sys.argv[1] == 'playback' and len(sys.argv) == 4:
        return playback(sys.argv[2], sys.argv[3])

    return 0

if __name__ == '__main__':
    main()
