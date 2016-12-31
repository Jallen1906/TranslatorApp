#!/usr/bin/python
import curses
import time
import translator
import pygtk
pygtk.require("2.0")
import gtk


def translateWord(trans, word):
    stdscr.addstr(1,0, origstr.format(""))
    stdscr.addstr(4,0, transtr.format(""))
    curses.setsyx(1,0)
    stdscr.clrtoeol()
    curses.setsyx(4,0)
    stdscr.clrtoeol()
    stdscr.addstr(1,0, origstr.format(word))
    stdscr.addstr(4,0, transtr.format(trans.translate(word)))

if __name__ == "__main__":
    googTrans = translator.GoogleApiTranslator("fr")
    
    stdscr = curses.initscr()
    curses.cbreak()
    quit = False
    origstr = "Original String:{}"
    transtr = "Translated Str :{}"
    stdscr.addstr(1,0, origstr.format(""))
    stdscr.addstr(4,0, transtr.format(""))


    stdscr.addstr(0,0, "Hit 't' to translate from clipboard or 'q' to quit")
    
    while quit != True:
        event = stdscr.getch()
        if event == ord("q"): quit = True
        if curses.keyname(event).lower()=="t":
            clipboard = gtk.clipboard_get()
            text = clipboard.wait_for_text()
            translateWord(googTrans, text)

               

    curses.endwin()

