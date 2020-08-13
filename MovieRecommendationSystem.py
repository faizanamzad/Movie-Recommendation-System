o# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 15:59:17 2019

@author: Faizan
"""

import numpy as np
import pandas as pd
#pd.set_option('display.expand_frame_repr', False)
#pd.set_option('display.height', 1000)
#pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)
ratings_data = pd.read_csv("G:/F/ML/MovieRecommendationSystem/ml-latest-small/ratings.csv")
#print(ratings_data.head())

movie_names = pd.read_csv("G:/F/ML/MovieRecommendationSystem/ml-latest-small/movies.csv")
#print(movie_names.head())

movie_data = pd.merge(ratings_data,movie_names,on='movieId')
#print(movie_data.head())

#print(movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head())

#print(movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head())
ratings_mean_count=movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head()  

ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts']=pd.DataFrame(movie_data.groupby('title')['rating'].count())
#print(ratings_mean_count.head())

user_movie_rating = movie_data.pivot_table(index='userId',columns='title',values='rating')
#print(user_movie_rating.head())

Forrest_Gump_ratings = user_movie_rating['Forrest Gump (1994)']
#print(Matrix_ratings.sort_values(ascending=False).head())

movies_like_Forrest_Gump = user_movie_rating.corrwith(Forrest_Gump_ratings)
corr_Forrest_Gump = pd.DataFrame(movies_like_Forrest_Gump,columns=['Correlation'])
corr_Forrest_Gump.dropna(inplace=True)
#print(corr_Matrix.head())

#print(corr_Matrix.sort_values('Correlation',ascending=False).head(15))
corr_Forrest_Gump = corr_Forrest_Gump.join(ratings_mean_count['rating_counts'])
print(corr_Forrest_Gump[corr_Forrest_Gump['rating_counts']>50].sort_values('Correlation',ascending=False).head())

