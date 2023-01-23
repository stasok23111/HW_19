from dao.movie_dao import MovieDao


class MovieService:

    def __init__(self, dao: MovieDao):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_director_id(self, did):
        return self.dao.get_by_director_id(did)

    def get_by_genre_id(self, gid):
        return self.dao.get_by_genre_id(gid)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def create(self, data):
        return self.dao.creat(data)

    def update(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.genre = data.get('genre')
        movie.year = data.get('year')
        movie.trailer = data.get('trailer')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        return self.dao.update(movie)

    def add_movie(self, data):
        new_movie = self.dao.creat(data)
        return new_movie

    def filters(self, data):
        if data.get('genre_id') is None:
            return self.dao.get_by_genre_id(data.get('genre_id'))
        elif data.get('director_id') is None:
            return self.dao.get_by_director_id(data.get('director_id'))

        elif data.get('year') is None:
            return self.dao.get_by_year(data.get('year'))

        else:
            return self.dao.get_all()

    def delete(self, mid):
        movie = self.get_one(mid)
        self.dao.delete(movie)
