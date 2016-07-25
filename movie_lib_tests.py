from rating import Rating
from user import User



def test_rating_class_initiation():
    rating_data_1 = [['196', '242', '3', '881250949'], ['186', '302', '3', '891717742'], ['22', '377', '1', '878887116'], ['244', '51', '2', '880606923'], ['166', '346', '1', '886397596'], ['298', '474', '4', '884182806'], ['115', '265', '2', '881171488'], ['253', '465', '5', '891628467'], ['305', '451', '3', '886324817'], ['6', '86', '3', '883603013']]

    rating1 = Rating(rating_data_1[0])

    assert rating1.user_id == 196
    assert rating1.movie_id == 242
    assert rating1.rating == 3
    assert rating1.time ==881250949

def test_movie_class_initiation():
    user_1 = ['1', '24', 'M', 'technician', '85711']

    user1 = User(user_1)

    assert user1.user_id == 1
    assert user1.age == 24
    assert user1.gender == 'M'
    assert user1.occupation == 'technician'
    assert user1.zipcode == '85711'
