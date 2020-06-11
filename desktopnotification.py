import feedparser
import notify2
import os
import time

def parseFeed():
    f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
    icon_path = os.getcwd() + "/icon.ico"
    notify2.init("news notify")
    for newsitem in f['items']:
         n = notify2.Notification(newsitem ['title'],newsitem['summary'],icon=icon_path)
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.show()
    n.set_timeout(15000)
    time.sleep(1200)
if __name__ == '__main__':
    parseFeed()
