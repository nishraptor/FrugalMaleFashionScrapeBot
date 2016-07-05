# FrugalMaleFashionScrapeBot
Web scraper that monitors /r/frugalmalefashion based on your preferences to stay on top of deals

Uses Praw and tkinter to filter /r/frugalmalefashion and to email you on deals YOU want as soon as they are posted.

TODO~

GUI:
  -Add remove button
  -List contents of the filter.txt file
  -Add Pause/Play Buttons
  -Add Remove All Preferences Button
  -Add Button to set time delay(for email)
  -Add help/more info features(README) in button form or something better

Logic:
  - Parse through submission text based on filter.txt file
  - Control time waited to generate results
  - Send email to user regarding deals
  - Generate history regarding deals such that the same deals are not sent multiple times. 

