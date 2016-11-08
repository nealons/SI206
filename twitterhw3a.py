# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy

access_token = "2993514232-ZFOQSjwBwT9Dj127B9rtHF2hkLgTRMHEY8f50Ch"
access_token_secret = "qeZH5nk5Rry4DlCSIoukvAl9BIGsFMmR24LxrTw5zD5fn"
consumer_key = "HSNLNuIvUjZ5NdKTZQ6Dpbeul"
consumer_secret = "bJ0w6JkanBdmLQN7B8Cyl7dw6RLvFFFqlbA65xKOPsBdrCiQvO"

auth1 = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth1.set_access_token(access_token,access_token_secret)

api_auth = tweepy.API(auth1)

status = "#UMSI206 #Proj3"
api_auth.update_with_media('Salad.jpg', status=status)