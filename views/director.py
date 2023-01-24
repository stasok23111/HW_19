from flask_restx import Resource, Namespace
from flask import request

from implemented import director_service, director_schema, directors_schema
from helpers.decorators import auth_required, admin_required

director_ns = Namespace('director')

@director_ns.route('/')
class DirectorView(Resource):
    @auth_required
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200
    @admin_required
    def post(self):
        data = request.json

        new_director = director_service.add_director(data)
        return '', 201, {'location':f'/director/{new_director}'}

@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        director = director_service.get_by_id(did)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, did):
        data= request.json

        data['id'] = did

        director_service.update(data)

        return 'updated', 204

    @admin_required
    def delete(self, did):

        director_service.delete(did)

        return 'deleted', 204
