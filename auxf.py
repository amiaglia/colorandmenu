import sys
import os

def del_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')