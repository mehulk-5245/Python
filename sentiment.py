#You need to install TextBlob Package first.
#try the command below
#pip install TextBlob
#If it doesn't work, try
#pip3 install TextBlob

#importing the downloaded TextBlob
from textblob import TextBlob

text = "Python is a very good language to learn"

obj = TextBlob(text)

#returns the sentiment of text
#by returning a value between -1.0 and 1.0
sentiment = obj.sentiment.polarity

print(sentiment)
