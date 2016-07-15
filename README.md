# FrugalMaleFashionScrapeBot
Web scraper that monitors /r/frugalmalefashion based on your preferences to stay on top of deals


Uses Praw and tkinter to filter /r/frugalmalefashion and to email you on deals you want as soon as they are posted, and uses fbchat in order to send you the deals.

Functionality:
  - Parse through submission text based on filter.txt file
  - Control time waited to generate results
  - Send Facebook Messages to user regarding deals
  - Generate history regarding deals such that the same deals are not sent multiple times. 
  - Start/Stop buttons.

TODO~
  - Layout Tkinter GUI in a better fashion
  - Add GUI input for facebook username/password
  - Add time intervals for scraping in GUI
  - Read through previous messages to make sure they are not sent twice


Any commits appreciated!
