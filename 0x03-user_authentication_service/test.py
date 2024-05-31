class DB:

    def add_user(self, email, hashed_password):
        user = User(email=email, hashed_password=hashed_password)
        self.session.add(user)
        self.session.commit()

    def find_user_by(self, **kwargs):
        if kwargs is None:
            raise Requesterror:
        columns = User.__table__.columns
        for key in kwargs:
            if key not in columns:
                raise requet error:
        user = self.session.query(user).filter_by(**kwargs).first()
        return user 
    
    def update_user(self, user_id, **kwargs):
        user = self.find_user_by(id=user_id)
        if user