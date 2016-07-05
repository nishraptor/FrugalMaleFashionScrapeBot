import praw

matches = ["jcrew","desert boots","j crew","j.crew","clarks","old navy"]


r = praw.Reddit(user_agent='Test Script by /u/nishraptor')
submission = r.get_subreddit("frugalmalefashion").get_top_from_day(limit=10)

submission = list(submission)
for sub in submission:
    print(sub.permalink)

l = []
#appends submission data in lowercase to a list
for x in submission:
    l.append(str(x).lower())

for x in l:
    print(x)
