from dao.models.user import User

class UserDAO:

    def __init__(self,session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_user_by_id(self, uid):
        return self.session.query(User).get(uid)
    def get_user_by_username(self,username):
        return self.session.query(User).filter(User.username == username).first()
    def create(self, user_d):
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()

        return user

    def update(self,user_d):
        user = self.get_user_by_id(user_d.get('id'))
        user.username = user_d.get('username')
        user.password = user_d.get('password')
        user.role = user_d.get('role')

        self.session.add()
        self.session.commit()

    def delete(self,uid):

        user = self.get_user_by_id(uid)

        self.session.delete(user)
        self.session.commit