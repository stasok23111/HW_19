from dao.movie_dao import MovieDao
from dao.genre_dao import GenreDao
from dao.director_dao import DirectorDao
from dao.user_dao import UserDAO

from service.movie_service import MovieService
from service.director_service import DirectorService
from service.genre_service import GenreService
from service.user_sevice import UserService
from service.auth import AuthService

from dao.models.movie import MovieSchema
from dao.models.genre import GenreSchema
from dao.models.director import DirectorSchema




from setup_db import db

director_dao = DirectorDao(session=db.session)
director_service = DirectorService(dao=director_dao)

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

movie_dao = MovieDao(session=db.session)
movie_service = MovieService(dao=movie_dao)

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

genre_dao = GenreDao(session=db.session)
genre_service = GenreService(dao=genre_dao)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

user_dao = UserDAO(session=db.session)
user_service = UserService(dao=user_dao)





auth_service = AuthService(user_service)