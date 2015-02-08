import praw
import time
import re

reddit = praw.Reddit(user_agent='RedditNewsLurker')

while True:
    subreddit = reddit.get_subreddit('worldnews')
    for submission in subreddit.get_rising(limit=10):
        match = re.search(r'^[1-9]+ ::', str(submission))
        if match:
            n = re.search(r'^[1-9]+', match.group())
            if n:
                score = int(n.group())
                news = re.sub(r'^[1-9]+ ::', '', str(submission))
                if score > 100:
                    print '!!!'
                    print 'BREAKING: ', news, ' Read more: ', submission.short_link
                    print '!!!'
                elif score > 50:
                    print 'Big News! ', news, ' Read more: ', submission.short_link
                elif score > 30:
                    print 'Medium news! ', news, ' Read more: ', submission.short_link
                elif score > 10:
                    print 'News! ', news, ' Read more: ', submission.short_link
    print 'Sleeping for 200s'
    time.sleep(200)