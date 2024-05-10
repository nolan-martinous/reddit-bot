import praw
import pdb
import re
import os

# create reddit instance using values in praw.ini
reddit = praw.Reddit('bot1')

# if there is not an existing posts replied to file
if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []

# if the file does exist: open and read it
else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

# selected subreddit
subreddit = reddit.subreddit('python')

# get the top 5 hot posts in the subreddit
for submission in subreddit.hot(limit=5):

	# if post has not been replied to
	if submission.id not in posts_replied_to:

		# check if post has target phrase
		if re.search("python", submission.title, re.IGNORECASE):

			# reply to post
			submission.reply("I love python! Ssssss")
			print("Bot replying to : ", submission.title)
			posts_replied_to.append(submission.id)

# add newly replied posts to posts replied to file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
    	f.write(post_id + "\n")
