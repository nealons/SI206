#Nealon Suthersan

# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob

access_token = "2993514232-ZFOQSjwBwT9Dj127B9rtHF2hkLgTRMHEY8f50Ch"
access_token_secret = "qeZH5nk5Rry4DlCSIoukvAl9BIGsFMmR24LxrTw5zD5fn"
consumer_key = "HSNLNuIvUjZ5NdKTZQ6Dpbeul"
consumer_secret = "bJ0w6JkanBdmLQN7B8Cyl7dw6RLvFFFqlbA65xKOPsBdrCiQvO"

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret) #basic OAuth code
auth1.set_access_token(access_token, access_token_secret)  #basic OAuth code continued

api = tweepy.API(auth1)

userinput = input("What tag do you want to search on Twitter? ") #raw input
publictweets = api.search(userinput) #searches API for what was inputted into raw input
polarity_acum = 0
subjectivity_acum = 0

tagtweets = [tweet10.text for tweet10 in publictweets]


print(tagtweets)

for tweets1 in tagtweets:
	tweetsblob_analysis = TextBlob(tweets1) #basic NLP language processing package
	subjectivity_acum += tweetsblob_analysis.subjectivity #finds subjectivities
	polarity_acum += tweetsblob_analysis.polarity #finds polarities
print("Average subjectivity is " + (str((subjectivity_acum)/len(tagtweets)))) #prints average
print("Average polarity is " + (str((polarity_acum)/len(tagtweets)))) #prints average
