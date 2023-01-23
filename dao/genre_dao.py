from .models.genre import Genre


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genres = self.session.query(Genre).all()
        return genres

    def get_one(self,gid):
        genre = self.session.query(Genre).get(gid)
        return genre
    def create(self, data):
        new_genre = Genre(**data)
        self.session.add(new_genre)
        self.session.commit()
        return new_genre

    def update(self,genre):
        self.session.add(genre)
        self.session.commit()
    def delete(self, genre):
        self.session.delete(genre)
        self.session.commit()