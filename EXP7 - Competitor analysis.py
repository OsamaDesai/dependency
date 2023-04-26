import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

samsung_data = pd.read_csv("C:/Users/nnair/Downloads/exp9 (comparitive analysis) - sentiment_analysis_samsung.csv")
apple_data = pd.read_csv("C:/Users/nnair/Downloads/exp9 (comparitive analysis) - sentiment_analysis_apple.csv")

samsung_sentiments = samsung_data.groupby('sentiment_label')['comment_text'].count()
apple_sentiments = apple_data.groupby('sentiment_label')['comment_text'].count()

fig, ax=plt.subplots()

samsung_sentiments.plot(kind='bar', ax=ax, position=0,width=0.4, label='Samsung',color='blue')
apple_sentiments.plot(kind='bar', ax=ax, position=1,width=0.4, label='Apple',color='orange')
ax.set_xlabel('Sentiment Label')

ax.set_ylabel('Nuber of Tweets')
ax.legend()
plt.show()