class Movie:
    def __init__(self, row):
        self.movie_id = int(row[0])
        self.title = row[1]
        self.video_date = row[2]
        self.link = row[4]
        self.genre = row[5:]

    def get_movie_name(movie_id, movie_data_list):
        for movie in movie_data_list:
            if movie.movie_id == movie_id:
                return movie.title
