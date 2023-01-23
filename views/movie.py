from flask import request
from flask_restx import Resource, Namespace

from implemented import movie_service, movie_schema, movies_schema

from helpers.decorators import auth_required, admin_required

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self):
        data = {
            'director_id': request.args.get('director_id'),
            'genre': request.args.get('genre_id'),
            'year': request.args.get('year')
        }
        all_movie = movie_service.filters(data)

        return movies_schema.dump(all_movie), 200

    @admin_required
    def post(self):
        data = request.json
        new_movie = movie_service.add_movie(data)
        return "", 201, {'location': f'/movie/{new_movie}'}

@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @auth_required
    def get(self,mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self,mid):
        data = request.json

        data['id'] = mid

        movie_service.update(data)

        return 'updated', 204

    @admin_required
    def delete(self, mid):

        movie_service.delete(mid)
        return 'deleted', 204