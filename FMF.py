import praw
from tkinter import *
from tkinter import messagebox
import errno
import threading
import fbchat


# global variable that keeps track of list of keywords
matches = []

#Global Variable that continues the thread
Run = False

# Function to refresh the filter.txt file and add to the global variable matches[] any new filter keywords
def refreshFile():
    global matches
    matches = []

    try:
        with open("filter.txt") as f:
            for line in f:
                matches.append(line)
            f.close()
    except IOError:
        f = open("filter.txt", "w+")
        f.close()

    matches = [item.rstrip() for item in matches]
    if len(matches) !=0:
        matches[:] = [x for x in matches if x != '']
        print("yes")
        print(matches)
        print("yes")


# End refreshFile()

# matches = ["jcrew", "desert boots", "j crew", "j.crew", "clarks", "old navy", "uniqlo"]
def checkForMatches():
    global matches
    global Run
    r = praw.Reddit(user_agent='Test Script by /u/nishraptor')
    submission = r.get_subreddit("frugalmalefashion").get_top_from_day(limit=10)

    submission = list(submission)

    client = fbchat.Client("username", "password")
    friends = client.getUsers("Nishant Mysore")  # return a list of names
    friend = friends[0]



    for sub in submission:
        for x in matches:
            if any(x in str(sub).lower() for x in matches):
                print(sub.permalink)
                sent = client.send(friend.uid, sub.permalink)

    if sent:
        print("Message sent successfully!")


    if Run:
        threading.Timer(10, checkForMatches).start()
    else:
        print("Run is False")

def stopThread():
    global Run
    Run = False

def startThread():
    global Run
    Run = True
    checkForMatches()

# Goal: Have the above code in a function. A button in the gui runs the function to check (every x minutes) for a match


#Start Gui
refreshFile()
top = Tk()
Lb1 = Listbox(top)

def refreshListbox():
    global Lb1
    i = 0
    Lb1.delete(0,END)
    for x in matches:
        if x != '' and len(x) != 0:
            Lb1.insert(i, x)
            i += 1
    Lb1.pack(side=RIGHT)

E1 = Entry(top, bd=5)

E1.pack(side=BOTTOM)


def OK():
    if(E1.get() != ''):

        with open("filter.txt", "a") as f:
            f.write("\n" + E1.get() + '\n')

        E1.delete(0, END)
        refreshFile()
        refreshListbox()
    else:
        pass

    print("")
    print(matches)
    print("")


def Remove():
    global matches
    if(E1.get() != '' and len(matches)!=0):

        f = open("filter.txt", 'w')
        for x in matches:
            if(x != E1.get()):
                f.write(x + '\n')
        E1.delete(0,END)
        f.close()
        refreshFile()
        refreshListbox()

    elif len(Lb1.curselection()) > 0:
        tup = Lb1.curselection()
        matches.pop(tup[0])
        refreshFile()
        refreshListbox()
    print("")
    print(matches)
    print("")

def Clear():
    global matches
    f = open("filter.txt",'w').close()
    refreshFile()
    print("")
    print(matches)
    print("")
    refreshListbox()

Lb1 = Listbox(top)

print("df")
print(matches)
print("df")


#Refresh the GUI
refreshListbox()

Add = Button(top, text="Add Keyword to \n Filter", command=OK)
Delete = Button(top, text = "Remove Keyword from \n Filter", command=Remove)
Clr = Button(top, text = "Remove all keywords",command = Clear)
Start = Button(top, text = "Start Bot", command  = startThread)
Stop = Button(top,text = "Stop Bot", command = stopThread)

Add.pack(side=LEFT)
Delete.pack(side = LEFT)
Clr.pack(side = LEFT)
Start.pack(side = LEFT)
Stop.pack(side = LEFT)
top.mainloop()


################################################## E N D G U I #########################################################
