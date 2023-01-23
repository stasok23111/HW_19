from .models.director import Director

class DirectorDao:

    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        director = self.session.query(Director).get(did)
        return director

    def get_all(self):
        directors = self.session.query(Director).all()
        return directors

    def create(self, data):
        new_director = Director(**data)
        self.session.add(new_director)
        self.session.commit()
        return new_director

    def update(self, director):
        self.session.add(directir)
        self.session.commit()

    def delete(self,director):
        self.session.delete(director)
        self.session.commit()
