from colored import fg, bg, attr
import time
from auxf import del_last_lines, clear

def loading(max = 50):
    print('%s[-]%s Your content is loading' % (fg('red'), attr('reset')))
    for i in range(1, max-1):
        print(f"%s[{'+'*i}%s{'-'*(max-2-i)}]%s" % (fg('green'), fg('red'), attr('reset')))
        time.sleep(0.25)
        del_last_lines()
    del_last_lines()
    print('%s[+]%s Your content is fully loaded' % (fg('green'), attr('reset')))
    print(f"%s[{'+' * (max-2)}]%s" % (fg('green'), attr('reset')))