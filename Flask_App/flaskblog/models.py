from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    gender = db.Column(db.String(20))
    terms_acceptance =db.Column(db.String(20))
    liabilty_acceptance=db.Column(db.String(100))
    # date = db.Column(db.DateTime(50))
    home_number1 = db.Column(db.String(20))
    home_number2 = db.Column(db.String(20))
    cell_phone = db.Column(db.String(20))
    attending_school = db.Column(db.String(30))
    guardian_cell1 = db.Column(db.String(20))
    guardian_cell2 = db.Column(db.String(20))
    accountholder_cell = db.Column(db.String(20))
    work_daytime_number = db.Column(db.String(20))
    next_of_kin = db.Column(db.String(50))
    next_of_kin_number = db.Column(db.String(20))
    medical_dental_history = db.Column(db.String(200))
    postal_address = db.Column(db.String(200))
    physical_address = db.Column(db.String(200))
    occupation=db.Column(db.String(100))
    surname_and_initials=db.Column(db.String(100))
    identity_number2=db.Column(db.String(20))
    cellphone_number2=db.Column(db.Integer)
    medical_aid_details=db.Column(db.String(300))
    dependent_number=db.Column(db.Integer)
    insurance_type=db.Column(db.String(120))
    employer=db.Column(db.String(100))
    doctor = db.Column(db.String(50))
    alternative_doctor = db.Column(db.String(50))
    identity_number = db.Column(db.String(20))
    language=db.Column(db.String(50))
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    email2 = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
