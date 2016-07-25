class Rating:
    def __init__(self, rating_data):
        self.user_id = int(rating_data[0])
        self.movie_id = int(rating_data[1])
        self.rating = int(rating_data[2])
        self.time = int(rating_data[3])

    def find_all_ratings_by_movie(movie_id, rating_object_list):
        return [rating_object.rating for rating_object in rating_object_list if rating_object.movie_id == movie_id]

    def find_all_ratings_by_user(user_id, rating_object_list):
        return [rating_object.rating for rating_object in rating_object_list if rating_object.user_id == user_id]

    def find_average_ratings(movie_id, rating_object_dict):
        average = sum(rating_object_dict[movie_id])/len(rating_object_dict[movie_id])
        return round(average, 2)
