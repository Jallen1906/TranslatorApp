#!/usr/bin/python
from Tkinter import*
import traceback
import time
import translator
import wordstorer
mainframetxt = "Hit 't' to translate from clipboard, 'w' for list of translations or 'q' to quit"
currentText = ""
currentTrans = ""
def translateWord(trans, word):
    clearScreen()
    T.insert("2.0", origstr.format(word))
    transword = trans.translate(word)
    T.insert("3.0", transtr.format(transword))
    return transword
def quitTrans():
    print "Entering quitTrans()"
    root.quit()
def printMainFrame():
    T.insert("1.0", mainframetxt)
def clearScreen():
    T.delete("1.0", "end")
    printMainFrame()
def onClick(event):
    global storeFlag, currentText, currentTrans
    print "Clicked {}".format(repr(event.char))
    keyChar = event.char
    if keyChar == 'q':
        quitTrans()
    if keyChar == 't' and not storeFlag:
        currentText = getClipboard()
        currentTrans = translateWord(googTrans, currentText)
        if currentTrans != "":
            T.insert("4.0", "Store word {}? [y][n]\n".format(currentText))
            storeFlag = True
    if storeFlag:
        if keyChar == 'y':
            wordstore.addEntry(currentText, currentTrans)
            T.insert("6.0", "Stored!\n")
            storeFlag = False
        if keyChar == 'n':
            T.insert("6.0", "Not stored\n")
            storeFlag = False
#                    stdscr.move(5,0)
#                    stdscr.clrtoeol()
#                    stdscr.addstr(5,0,"Stored!")
def getClipboard():
    return root.selection_get(selection="CLIPBOARD")
if __name__ == "__main__":
    googTrans = translator.GoogleApiTranslator("fr")
    
    # Variables
    storeFlag = False
    quit = False
    # Initialise screen
    root = Tk()
    S = Scrollbar(root)
    T = Text(root, height = 40, width=len(mainframetxt))
    S.pack(side=RIGHT, fill=Y)
    T.bind("<Key>", onClick)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    
    
    origstr = "Original String:{}\n"
    transtr = "Translated Str :{}\n"
    
    T.insert("2.0", origstr.format(""))
    T.insert("3.0", transtr.format(""))
    
    wordstore = wordstorer.OfflineWordStorer("fr")
    printMainFrame()
    
    
    mainloop()
        
#    try:
#        while quit != True:
#            event = stdscr.getch()
#            if event == ord("q"): quit = True
#            if curses.keyname(event).lower()=="t" and not storeFlag:
#                clipboard = gtk.clipboard_get()
#                text = clipboard.wait_for_text()
#                transword = translateWord(googTrans, text)
#                if transword != "":
#                    stdscr.addstr(5,0,"Store word {}? [y][n]".format(text))
#                    storeFlag = True
#            if storeFlag and curses.keyname(event).lower() =='y':
#                storeFlag = False
#                try:
#                    wordstore.addEntry(text, transword)
#                    stdscr.move(5,0)
#                    stdscr.clrtoeol()
#                    stdscr.addstr(5,0,"Stored!")
#                    stdscr.refresh()
#
#                except TypeError:
#                    stdscr.move(5,0)
#                    stdscr.clrtoeol()
#                    stdscr.addstr(5,0,"Unable to store")
#                    
#            if storeFlag and curses.keyname(event).lower() =='n':
#                storeFlag = False
#                stdscr.move(5,0)
#                stdscr.clrtoeol()
#                stdscr.addstr(5,0,"Not stored")
#                stdscr.refresh()
#      
#            if curses.keyname(event).lower()=="w" and not storeFlag:
#                localentries = wordstore.getEntries()
#                list1 = []
#                list2 = []
#                # Word lengths
#                maxl1 = 0
#                maxl2 = 0
#                current_y_index = 8
#                for l1, l2 in localentries.iteritems():
#                    list1.append(l1)
#                    list2.append(l2)
#                    if maxl1 < len(l1):
#                        maxl1 = len(l1)
#                    if maxl2 < len(l2):
#                        maxl2 = len(l2)
#    #            x_boundary = max(len(origstr),len(transtr)) + (maxl1 if len(origstr) > len(transtr) else maxl2)
#                stdscr.move(current_y_index, 0)
#                stdscr.clrtoeol()
#                stdscr.refresh()
#                stdscr.addstr(current_y_index, 0, "{:{max1}s} {:{max2}s}".format("French","English", max1=maxl1,max2=maxl2 ))
#                #stdscr.addstr(current_y_index, 0, "{:15s} {:15s}".format("French","English" ))
#                for l1, l2 in zip(list1, list2):
#                    current_y_index += 1
#                    stdscr.move(current_y_index, 0)
#                    stdscr.clrtoeol()
#                    stdscr.refresh()
# #                   stdscr.addstr(current_y_index, 0, "{:15s} {:15s}".format(l1,l2))
#                    stdscr.addstr(current_y_index, 0, "{:{max1}s} {:{max2}s}".format(l1,l2, max1=maxl1, max2=maxl2 ))
#    except: 
#        quitTrans()
#        traceback.print_exc() 
#    quitTrans()                
                

