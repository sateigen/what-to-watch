class Rating:
    def __init__(self, rating_data):
        self.user_id = int(rating_data[0])
        self.movie_id = int(rating_data[1])
        self.rating = int(rating_data[2])
        self.time = int(rating_data[3])
