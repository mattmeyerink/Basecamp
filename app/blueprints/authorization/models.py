from datetime import datetime
from flask_login import UserMixin
from app import login, db


class User(UserMixin, db.Model):
    """Represents a user. Fields will be obtained through google auth."""
    __tablename__ = "Basecamp-Users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    name = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<User: {self.id} | {self.email}>"
    
    def from_dict(self, data):
        for field in ["email", "name"]:
            if field in data:
                setattr(self, field, data[field])

@login.user_loader
def load_user(id):
    """Query the db for user object."""
    return User.query.get(int(id))
