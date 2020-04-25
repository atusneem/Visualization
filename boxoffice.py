#Ayra Tusneem
#CPSC 392-02
#Assignment 01

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn

data = pd.read_csv("imdb.csv")

print(data.head())

print(data.shape)

data['title_year'].hist()

data['content_rating'].value_counts().plot(kind='bar')

comparison=pd.DataFrame(data[['gross','budget']])
plt.show()
data.plot(x='duration', y='imdb_score', kind='scatter')
plt.show()
data.plot(x='genres', y='gross', kind='line')
plt.show()
data.plot(x='imdb_score', y='movie_facebook_likes', kind='scatter')
plt.show()
seaborn.lmplot("director_facebook_likes", "gross", data=data, fit_reg=False)
plt.show()
