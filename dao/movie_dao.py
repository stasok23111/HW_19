from .models.movie import Movie


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        all_movie = self.session.query(Movie).all()
        return all_movie

    def get_one(self, mid):
        movie = self.session.query(Movie).get(mid)
        return movie

    def get_by_director_id(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre_id(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()


    def creat(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()

