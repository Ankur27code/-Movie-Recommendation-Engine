import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def get_title_from_index(index):
	return Df[Df.index == index]["title"].values[0]

def get_index_from_title(title):
	return Df[Df.title == title]["index"].values[0]

Df= pd.read_csv("movie_dataset.csv")
features = ['genres']
for feature in features:
	Df[feature] = Df[feature].fillna('')
cv = CountVectorizer()
count_matrix = cv.fit_transform(Df["genres"])
cosine_sim = cosine_similarity(count_matrix) 
movie_user_likes = "Avatar"
movie_index = get_index_from_title(movie_user_likes)
similar_movies =  list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)
i=0
for element in sorted_similar_movies:
		print (get_title_from_index(element[0]))
		i=i+1
		if i>50:
			break