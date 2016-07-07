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
        matches[:] = [x for x in matches if x != '']
        print("yes")
        print(matches)
        print("yes")


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


refreshListbox()

Add = Button(top, text="Add Keyword to \n Filter", command=OK)
Delete = Button(top, text = "Remove Keyword from \n Filter", command=Remove)
Clr = Button(top, text = "Remove all keywords",command = Clear)
Add.pack(side=LEFT)
Delete.pack(side = LEFT)
Clr.pack(side = LEFT)
top.mainloop()

################################################## E N D G U I #########################################################
