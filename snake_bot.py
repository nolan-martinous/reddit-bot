import random
import praw
import pdb
import re
import os

kaa_quotes = ["SsssSSssSS sssss SSs ss SSS ss SSSSSSS",
				"ssssss sssss SS ssss SSSssSSssSSssssss",
				"SSSSSSS ssss SSSSSSssssSSSss sssssssSS"]

# create reddit instance using values in praw.ini
reddit = praw.Reddit('bot1')

# selected subreddit
subreddit = reddit.subreddit("snakes")

# monitor every comment in every post of the subreddit unit program is killed
for comment in subreddit.stream.comments():

	# if comment has search string
	if re.search("Kaa can you translate this post?", comment.body, re.IGNORECASE):

		# reply to comment
		kaa_reply = "🐍: " + random.choice(kaa_quotes)
		comment.reply(kaa_reply)

