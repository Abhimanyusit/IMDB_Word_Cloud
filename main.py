import pandas as pd
import re
from wordcloud import STOPWORDS
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('./content/IMDB-Dataset.csv')

#clean the text data
text = ' '.join(df['review'].astype(str).tolist())
text = re.sub(r'[^A-Za-z\s]', '', text)
text = text.lower()
sw = set(STOPWORDS)
text = ' '.join(word for word in text.split() if word not in sw)

#Generate the word cloud image
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of IMDB Reviews')
plt.show()