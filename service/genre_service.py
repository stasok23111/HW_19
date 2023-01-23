from dao.genre_dao import GenreDao


class GenreService:
    def __init__(self, dao: GenreDao):
        self.dao = dao

    def get_all(self):
        all_genres = self.dao.get_all()
        return all_genres

    def get_by_id(self, gid):
        genre = self.dao.get_one(gid)
        return genre
    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        gid = data.get('id')
        genre = self.get_by_id(gid)

        genre.name = data.get('name')

        return self.dao.update(genre)

    def delete(self,gid):
        genre = self.get_by_id(gid)
        self.dao.delete(genre)

    def add_genre(self, data):
        new_genre = self.dao.create(data)
        return new_genre