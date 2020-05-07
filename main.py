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
    max = 50
    print('%s[-]%s Your content is loading' % (fg('red'), attr('reset')))
    for i in range(1, max-1):
        print(f"%s[{'+'*i}%s{'-'*(max-2-i)}]%s" % (fg('green'), fg('red'), attr('reset')))
        time.sleep(0.25)
        del_last_lines()
    del_last_lines()
    print('%s[+]%s Your content is fully loaded' % (fg('green'), attr('reset')))
    print(f"%s[{'+' * (max-2)}]%s" % (fg('green'), attr('reset')))

def menu():
    print('%s1.%s Loading example' % (fg('red'), attr('reset')))
    print('%s0.%s Exit' % (fg('red'), attr('reset')))

    choice = int(input())
    clear()

    if choice == 1:
        loading()



clear()
menu()