import praw

# reddit instance using saved values in praw.ini
reddit = praw.Reddit('bot1')

# selected subreddit
subreddit = reddit.subreddit("learnpython")

# get the top 5 hot submission in the subreddit
for submission in subreddit.hot(limit=5):
	print("Title: ", submission.title)
	print("Text: ", submission.selftext)
	print("Score: ", submission.score)
	print("---------------------------------\n")

