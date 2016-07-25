import csv
from movie import Movie
from rating import Rating
from user import User

all_rating_data = []
movie_ratings = {}
user_ratings = {}

with open('ml-100k/u.data') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        ratings = Rating(row)
        all_rating_data.append(ratings)
        if ratings.user_id not in user_ratings:
            user_ratings[int(ratings.user_id)] = [int(ratings.rating)]
        else:
            user_ratings[int(ratings.user_id)].append(int(ratings.rating))

        if ratings.movie_id not in movie_ratings:
            movie_ratings[int(ratings.movie_id)] = [int(ratings.rating)]
        else:
            movie_ratings[int(ratings.movie_id)].append(int(ratings.rating))

user_data = []

with open('ml-100k/u.user') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        user = User(row)
        user_data.append(user)

movie_data = []

with open('ml-100k/u.item') as f:
    reader = csv.reader(f, delimiter="|")
    for row in reader:
        movie = Movie(row)
        movie_data.append(movie)
