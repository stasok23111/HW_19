from dao.director_dao import DirectorDao


class DirectorService:
    def __init__(self, dao: DirectorDao):
        self.dao = dao

    def get_by_id(self, did):
        director = self.dao.get_one(did)
        return director

    def get_all(self):
        directors = self.dao.get_all()
        return directors
    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        did = data.get('id')
        directior = self.get_by_id(did)

        director.name = data.get('name')

        return self.dao.update(directior)

    def delete(self, did):
        directir = self.get_by_id(did)
        self.dao.delete(directir)

    def add_director(self, data):
        new_director = self.dao.create(data)
        return new_director