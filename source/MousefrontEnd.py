#!/usr/bin/python
import curses
import time
transTxt = "Click in this box to translate contents of clipboard"
transBrd = "="*(len(transTxt) + 2)
transBx = transBrd + "\n" + "|" + transTxt + "|\n" + transBrd

quitTxt = "Click in this box to quit"
quitBrd = "="*(len(quitTxt) + 2)
quitBx = quitBrd + "\n" + "|" + quitTxt + "|\n" +quitBrd
def createCoordsBx(x,y):
    coordsTxt =    "X Position : {}|\n|Y Position : {}".format(x, y)
    coordsBrd = "="*(len(coordsTxt)/2 + 2)
    return coordsBrd + "\n" + "|" + coordsTxt + "|\n" + coordsBrd

'''
========================================================
||Click in this box to translate contents of clipboard||
========================================================
'''

if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.curs_set(0) 
    stdscr.keypad(1) 
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    quit = False

    stdscr.addstr(transBx)

    stdscr.addstr(3,0,quitBx)
    
    stdscr.addstr(6,0,createCoordsBx(0,0))
    clickcount = 0
    while quit != True:
        event = stdscr.getch()
        if event == ord("q"): quit = True
        if event == curses.KEY_MOUSE:
            '''clickcount += 1
            stdscr.addstr(12,0, "Mouse click {}".format(clickcount))
            _, mx, my, _, _ = curses.getmouse()
            y, x = stdscr.getyx()
            stdscr.addstr(6,0,createCoordsBx(x,y))
            stdscr.refresh()
'''
            _, mx, my, _, _ = curses.getmouse()
            y, x = stdscr.getyx()
            if x >= 0 and x < len(transBrd) and y >= 0 and y < 3:
                stdscr.addstr(12, 0, "Translate here")
            elif x >= 0 and x < len(quitBrd) and y >= 3 and y < 6:
                stdscr.addstr(12,0,"Quit")
                curses.endwin()
                quit = True
            else:
                for a in range(2):
                    stdscr.addstr(12,0,"Missed!")
                    time.sleep(0.5)
                    stdscr.addstr(12,0,"Me     ")
                    time.sleep(0.5)

