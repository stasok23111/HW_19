from flask_restx import Resource, Namespace

from implemented import genre_service, genre_schema, genres_schema
from flask import request
from helpers.decorators import admin_required, auth_required

genre_ns = Namespace('genres')

@genre_ns.route('/')
class GenreView(Resource):
    @auth_required
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

    @admin_required
    def post(self):
        data = request.json

        new_genre = genre_service.add_genre(data)
        return '', 201, {'location': f'/genre/{new_genre}'}

@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_by_id(gid)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, gid):
        data = request.json

        data['id'] = gid

        genre_service.update(data)

        return 'updatetd', 204

    @admin_required
    def delete(self, gid):

        genre_service.delete(gid)

        return 'deleted', 204

