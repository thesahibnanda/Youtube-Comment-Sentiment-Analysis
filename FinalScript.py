#Final File To Run The Script
import pandas as pd
import numpy as np
#Importing Other Python Files
from YouTubeCommentScraper import YouTube_Comment
from PreprocessingData import Clean_Text
from SentimentAndSeverityAnalysis import Function_Sentiment, Function_Severity

#Scraping Comments
url = input("Enter YouTube Link: ")
comments = YouTube_Comment(url) #Returns List

Cleaned_Comments = []

#Preprocessing Data
for comment in comments:
    cleaned  = Clean_Text(comment)
    Cleaned_Comments.append(cleaned)

Sentiment = []
Severity = []
Score = []

for clean in Cleaned_Comments:
    senti_score= Function_Sentiment(clean) #Returns Tuple With Sentiment At Index 0 And Score At Index 1
    senti = senti_score[0]
    scor = senti_score[1]
    sever = Function_Severity(clean) #Returns String
    Sentiment.append(senti)
    Score.append(scor)
    Severity.append(sever)

Full_Analytics = pd.DataFrame({
    'Comment': comments,
    'Sentiment': Sentiment,
    'Score': Score,
    'Severity': Severity
})

Full_Analytics.to_csv("Analytics.csv")

print("\n")#Leaving A Line To Improve Presentation
print("\n")#Leaving A Line To Improve Presentation

print("Average Score: " , sum(Score)/len(Score))
print("Total Positive Sentiment Comments: ", Sentiment.count('POSITIVE'))
print("Total Negative Sentiment Comments: ", Sentiment.count('NEGATIVE'))
if Sentiment.count('POSITIVE') >=Sentiment.count('NEGATIVE'):
    print("Average Severity: Not Severe")
else:
    print("Average Severity: ", Function_Severity(sum(Score)/len(Score)))
    


