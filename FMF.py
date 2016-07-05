import praw
from tkinter import *
import errno

matches = []

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

refreshFile()
print("")
print(matches)
print("")

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


#Goal: Have the above code in a function. A button in the gui runs the function to check (every x minutes) for a match


###############################################S T A R T G U I#########################################################

top = Tk()


E1 = Entry(top, bd=5)

E1.pack(side=BOTTOM)


def callback():
    with open("filter.txt","a") as f:
        f.write("\n")
        f.write(E1.get())

    E1.delete(0, END)
    refreshFile()

    print("")
    print(matches)
    print("")

OK = Button(top, text="Add text to \n Filter", command=callback)


OK.pack(side =LEFT)


top.mainloop()

################################################## E N D G U I#########################################################

