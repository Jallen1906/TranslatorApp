#!/usr/bin/python
import curses
import traceback
import time
import translator
import pygtk
pygtk.require("2.0")
import gtk
import wordstorer

def translateWord(trans, word):
    clearScreen()
    stdscr.addstr(1,0, origstr.format(word))
    transword = trans.translate(word)
    stdscr.addstr(4,0, transtr.format(transword))
    return transword
def quitTrans():
    clearScreen()
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
def printMainFrame():
    stdscr.addstr(0,0, "Hit 't' to translate from clipboard, 'w' for list of translations or 'q' to quit")
def clearScreen():
    stdscr.erase()
    stdscr.refresh()
    printMainFrame()
if __name__ == "__main__":
    googTrans = translator.GoogleApiTranslator("fr")
    
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    quit = False
    origstr = "Original String:{}"
    transtr = "Translated Str :{}"
    stdscr.addstr(1,0, origstr.format(""))
    stdscr.addstr(4,0, transtr.format(""))
    wordstore = wordstorer.OfflineWordStorer("fr")
    printMainFrame()
    storeFlag = False
    try:
        while quit != True:
            event = stdscr.getch()
            if event == ord("q"): quit = True
            if curses.keyname(event).lower()=="t" and not storeFlag:
                clipboard = gtk.clipboard_get()
                text = clipboard.wait_for_text()
                transword = translateWord(googTrans, text)
                if transword != "":
                    stdscr.addstr(5,0,"Store word {}? [y][n]".format(text))
                    storeFlag = True
            if storeFlag and curses.keyname(event).lower() =='y':
                storeFlag = False
                try:
                    wordstore.addEntry(text, transword)
                    stdscr.move(5,0)
                    stdscr.clrtoeol()
                    stdscr.addstr(5,0,"Stored!")
                    stdscr.refresh()

                except TypeError:
                    stdscr.move(5,0)
                    stdscr.clrtoeol()
                    stdscr.addstr(5,0,"Unable to store")
                    
            if storeFlag and curses.keyname(event).lower() =='n':
                storeFlag = False
                stdscr.move(5,0)
                stdscr.clrtoeol()
                stdscr.addstr(5,0,"Not stored")
                stdscr.refresh()
      
            if curses.keyname(event).lower()=="w" and not storeFlag:
                localentries = wordstore.getEntries()
                list1 = []
                list2 = []
                # Word lengths
                maxl1 = 0
                maxl2 = 0
                current_y_index = 8
                for l1, l2 in localentries.iteritems():
                    list1.append(l1)
                    list2.append(l2)
                    if maxl1 < len(l1):
                        maxl1 = len(l1)
                    if maxl2 < len(l2):
                        maxl2 = len(l2)
    #            x_boundary = max(len(origstr),len(transtr)) + (maxl1 if len(origstr) > len(transtr) else maxl2)
                stdscr.move(current_y_index, 0)
                stdscr.clrtoeol()
                stdscr.refresh()
                stdscr.addstr(current_y_index, 0, "{:{max1}s} {:{max2}s}".format("French","English", max1=maxl1,max2=maxl2 ))
                #stdscr.addstr(current_y_index, 0, "{:15s} {:15s}".format("French","English" ))
                for l1, l2 in zip(list1, list2):
                    current_y_index += 1
                    stdscr.move(current_y_index, 0)
                    stdscr.clrtoeol()
                    stdscr.refresh()
 #                   stdscr.addstr(current_y_index, 0, "{:15s} {:15s}".format(l1,l2))
                    stdscr.addstr(current_y_index, 0, "{:{max1}s} {:{max2}s}".format(l1,l2, max1=maxl1, max2=maxl2 ))
    except: 
        quitTrans()
        traceback.print_exc() 
    quitTrans()                
                

