class User:
    def __init__(self, row):
        self.user_id = int(row[0])
        self.age = int(row[1])
        self.gender = row[2]
        self.occupation = row[3]
        self.zipcode = row[4]
