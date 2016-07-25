from movie import Movie
from rating import Rating
from user import User


def test_rating_class_initiation():
    rating_data_1 = [['196', '242', '3', '881250949'], ['186', '302', '3', '891717742'], ['22', '377', '1', '878887116'], ['244', '51', '2', '880606923'], ['166', '346', '1', '886397596'], ['298', '474', '4', '884182806'], ['115', '265', '2', '881171488'], ['253', '465', '5', '891628467'], ['305', '451', '3', '886324817'], ['6', '86', '3', '883603013']]
    rating1 = Rating(rating_data_1[0])

    assert rating1.user_id == 196
    assert rating1.movie_id == 242
    assert rating1.rating == 3
    assert rating1.time == 881250949


def test_movie_class_initiation():
    user_1 = ['1', '24', 'M', 'technician', '85711']
    user1 = User(user_1)

    assert user1.user_id == 1
    assert user1.age == 24
    assert user1.gender == 'M'
    assert user1.occupation == 'technician'
    assert user1.zipcode == '85711'


def test_movie_class_initiation():
    movie_1 = ['1', 'Toy Story (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    movie1 = Movie(movie_1)

    assert movie1.movie_id == 1
    assert movie1.title == 'Toy Story (1995)'
    assert movie1.video_date == '01-Jan-1995'
    assert movie1.link == 'http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)'
    assert movie1.genre == ['0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']


def test_get_name_method_in_movie_class():
    movie_data_1 = [['1', 'Toy Story (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['2', 'GoldenEye (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?GoldenEye%20(1995)', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'], ['3', 'Four Rooms (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Four%20Rooms%20(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'], ['4', 'Get Shorty (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Get%20Shorty%20(1995)', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['5', 'Copycat (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Copycat%20(1995)', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'], ['6', 'Shanghai Triad (Yao a yao yao dao waipo qiao) (1995)', '01-Jan-1995', '', 'http://us.imdb.com/Title?Yao+a+yao+yao+dao+waipo+qiao+(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['7', 'Twelve Monkeys (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Twelve%20Monkeys%20(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0'], ['8', 'Babe (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Babe%20(1995)', '0', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['9', 'Dead Man Walking (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Dead%20Man%20Walking%20(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['10', 'Richard III (1995)', '22-Jan-1996', '', 'http://us.imdb.com/M/title-exact?Richard%20III%20(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0']]
    movie_objects = [Movie(movie) for movie in movie_data_1]

    assert Movie.get_movie_name(1, movie_objects) == 'Toy Story (1995)'
