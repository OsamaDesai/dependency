from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/content/exp10 (negative review) - pocoreview.csv')

# Concatenate all reviews into a single string
text = ''.join(df['review'])

# Print the concatenated string
print(text)

wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)


# Display the generated image
plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

# Show the plot
plt.show()