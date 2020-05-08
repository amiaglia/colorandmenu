from colored import fg, bg, attr
import os
import time
from loading import loading
from auxf import del_last_lines, clear

def menu():
    print('%s1.%s Loading example' % (fg('red'), attr('reset')))
    print('%s0.%s Exit' % (fg('red'), attr('reset')))

    choice = int(input())
    clear()

    if choice == 1:
        loading()



clear()
menu()