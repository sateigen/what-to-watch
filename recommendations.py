from rating import Rating
from movie import Movie
from user import User
from parse_data import all_rating_data, movie_ratings, user_ratings, user_data, movie_data
import operator

# finds movies that have more than a certain number of ratings
def scale_movies(movie_ratings_dict, number_of_rates):
    return [movie for movie in movie_ratings_dict if len(movie_ratings_dict[movie]) >= number_of_rates]


# connect average rating with scaled movie list
def connect_avg_to_movie_id(movie_ratings_list, movie_ratings_dict):
    return sorted([(int(movie_id), Rating.find_average_ratings(movie_id, movie_ratings_dict)) for movie_id in movie_ratings_list], key=operator.itemgetter(1))


def get_top_titles(movie_tuple_list, movie_data_list):
    top_list = movie_tuple_list[-25:]
    return [(Movie.get_movie_name(int(movie[0]), movie_data_list), movie[1]) for movie in top_list]
