import seaborn as sns
import numpy as np
import pandas as pd
import nltk

df = pd.read_csv('Exp3_twitter-sentiment-analysis.csv')

nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia= SentimentIntensityAnalyzer()

#print(df.head())

df['scores']=df['tweet'].apply(lambda tweet: sia.polarity_scores(str(tweet)))

#print(df.head())

df['compound']=df['scores'].apply(lambda score_dict:score_dict['compound'])
df.head()
df['pos']=df['scores'].apply(lambda pos_dict:pos_dict['pos'])
df.head()
df['neg']=df['scores'].apply(lambda neg_dict:neg_dict['neg'])


#print(df.head())

df['type']=''
df.loc[df.compound>0,'type']='POS'
df.loc[df.compound==0,'type']='NEUTRAL'
df.loc[df.compound<0,'type']='NEG'

#print(df.head())

len=df.shape
(rows,cols)=len
pos=0
neg=0
neutral=0
for i in range(0,rows): 
    if df.loc[i][7]=="POS":
        pos=pos+1
    if df.loc[i][7]=="NEG":
        neg=neg+1
    if df.loc[i][7]=="NEUTRAL":
        neutral=neutral+1
print("Positive :"+str(pos) + "  Negative :" + str(neg) + "   Neutral :"+ str(neutral))

