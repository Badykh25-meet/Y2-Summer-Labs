title = input("what is the name of your video?")
description = input("what is your video about?")
def create_youtube_video(title, description):
	new_video = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments" : {"username" : "", "comment_text":""}}
	return new_video
def like(new_video):
	if "likes" in new_video:
		new_video["likes"] += 1

def dislike(new_video):
	if "dislikes" in new_video:
		new_video["dislikes"] += 1

vid = create_youtube_video(title,description)
def addcomment(new_video, username, comment_text):
	new_video["comment"]["username"] = username
	new_video["comment"]["comment_text"] = comment_text
print(create_youtube_video)