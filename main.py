from colored import fg, bg, attr
import os
import sys
import time

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def del_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

def loading():
    pass

def menu():
    print('%s1.%s Loading example' % (fg('red'), attr('reset')))
    print('%s0.%s Exit' % (fg('red'), attr('reset')))

    choice = int(input())
    clear()

    if choice == 1:
        loading()



clear()
menu()