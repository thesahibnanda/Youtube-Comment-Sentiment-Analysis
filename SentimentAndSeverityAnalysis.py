#Sentiment Analysis And Severity Analysis
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

#Variablizing
classifier = pipeline("sentiment-analysis")
data = pd.read_csv("Score_Dataset.csv")
x = data[["score"]]
y = data[["severity"]]
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.18) 
logistic_regression_model = LogisticRegression(random_state=0).fit(xtrain, ytrain)

#Sentiment
def Function_Sentiment(news:str):
  res = classifier(news)
  sentiment = res[0]['label']
  score = (res[0]['score'])*100
  return (sentiment, score)

#Severity
def Function_Severity(news:str):
  l = Function_Sentiment(news)[1]
  r = Function_Sentiment(news)[0]
  if r == "POSITIVE":
    pred = ["Not Severe"]
  else:
    scalar_array = np.array([l])
    reshaped_array = scalar_array.reshape(1, -1)
    pred = logistic_regression_model.predict(reshaped_array)
  return pred[0]

