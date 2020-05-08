from colored import fg, bg, attr
import os
import sys
import time
from modules.loading import loading
from modules.auxf import del_last_lines, clear
from modules.help import printHelp

def menu():
    print('%s1.%s Loading example' % (fg('red'), attr('reset')))
    print('%s0.%s Exit' % (fg('red'), attr('reset')))

    choice = int(input())
    clear()

    if choice == 1:
        loading()

def argflags():
    args = sys.argv[1:]
    if len(args) == 0:
        menu()
    elif len(args) == 1:
        if args[0] == '-h' or args[0]=='--help':
            printHelp()
        elif args[0] == '-l':
            loading()
        elif args[0] == '-m':
            menu()
        else:
            print('Invalid option')
            printHelp()


if __name__ == "__main__":
    clear()
    argflags()