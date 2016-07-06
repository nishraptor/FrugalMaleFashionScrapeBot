import praw
from tkinter import *
import errno
from tkinter import messagebox

# global variable that keeps track of list of keywords
matches = []

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
        matches.remove('')


# End refreshFile()

# matches = ["jcrew", "desert boots", "j crew", "j.crew", "clarks", "old navy", "uniqlo"]

r = praw.Reddit(user_agent='Test Script by /u/nishraptor')
submission = r.get_subreddit("frugalmalefashion").get_top_from_day(limit=10)

submission = list(submission)
for sub in submission:
    print(sub.permalink)

l = []
# appends submission data in lowercase to a list
for x in submission:
    l.append(str(x).lower())

for x in l:
    print(x)

# Goal: Have the above code in a function. A button in the gui runs the function to check (every x minutes) for a match


############################################### S T A R T G U I #######################################################

top = Tk()

E1 = Entry(top, bd=5)

E1.pack(side=BOTTOM)


def OK():
    if(E1.get() != ''):

        with open("filter.txt", "a") as f:
            f.write("\n" + E1.get() + '\n')

        E1.delete(0, END)
        refreshFile()

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

    else:
        pass

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

Add = Button(top, text="Add Keyword to \n Filter", command=OK)
Delete = Button(top, text = "Remove Keyword from \n Filter", command=Remove)
Clr = Button(top, text = "Remove all keywords",command = Clear)
Add.pack(side=LEFT)
Delete.pack(side = LEFT)
Clr.pack(side = LEFT)
top.mainloop()

################################################## E N D G U I #########################################################
