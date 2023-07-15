from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text, create_engine, ForeignKey
from flask_login import UserMixin

Base = declarative_base()

# from app import db, login

# class User(Base, db.Model, UserMixin):
       
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

#     def __repr__(self):
#         return '<User {}>'.format(self.username) 
        
#     __bind_key__ = 'auth'
    
#     __tablename__ = 'user'
    
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(30), nullable=False, unique=True)
#     password_hash = db.Column(db.String(255), nullable=False)
    
# @login.user_loader
# def load_user(id):
#     return User.query.get(id)


class User(Base):
       
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username) 
        
    __bind_key__ = 'auth'
    
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    # password_hash = Column(String(255), nullable=False)
    password_hash = Column(String(255))

class BLOCK(Base):
    __tablename__ = 'BLOCK'
    
    ID = Column(Integer, primary_key=True)
    BLOCK = Column(String(9))
    START_DATE = Column(DateTime)
    END_DATE = Column(DateTime)
    AY = Column(String(9))
    
class CLERKSHIP(Base):
    __tablename__ = 'CLERKSHIP'
    
    CLERKSHIP_ID = Column(Integer, primary_key=True)
    CLERKSHIP = Column(Text)
    CLERKSHIP_ABBR = Column(String(10))
    
class LOCATION(Base):
    __tablename__ = 'LOCATION'
    
    LOCATION_ID = Column(Integer, primary_key=True)
    LOCATION = Column(Text)
    SITE_ABBRE = Column(Text)
    
class QUESTION(Base):
    __tablename__ = 'QUESTION'
    
    QUESTION_ID = Column(Integer, primary_key=True)
    QUESTION = Column(Text)


class EVAL(Base):
    __tablename__ = 'EVAL'
    
    EVAL_ID = Column(Integer, primary_key=True)
    GRADUATING_CLASS_YEAR = Column(Integer)
    BLOCK_NUMBER = Column(Integer)
    CLERKSHIP_NAME = Column(Integer)
    ACADEMIC_YEAR = Column(String(9))
    CLERKSHIP_LOCATION = Column(Integer)
    
    Q1 = Column(Integer)
    A1 = Column(Integer)
    Q2 = Column(Integer)
    A2 = Column(Integer)
    Q3 = Column(Integer)
    A3 = Column(Integer)
    Q4 = Column(Integer)
    A4 = Column(Integer)
    Q5 = Column(Integer)
    A5 = Column(Text)
    Q6 = Column(Integer)
    A6 = Column(Text)
    Q7 = Column(Integer)
    A7 = Column(Integer)
    Q8 = Column(Integer)
    A8 = Column(Integer)
    Q9 = Column(Integer)
    A9 = Column(Integer)
    Q10 = Column(Integer)
    A10 = Column(Integer)
    Q11 = Column(Integer)
    A11 = Column(Integer)
    Q12 = Column(Integer)
    A12 = Column(Integer)
    Q13 = Column(Integer)
    A13 = Column(Integer)
    Q14 = Column(Integer)
    A14 = Column(Integer)
    Q15 = Column(Integer)
    A15 = Column(Integer)
    Q16 = Column(Integer)
    A16 = Column(Integer)
    Q17 = Column(Integer)
    A17 = Column(Integer)
    Q18 = Column(Integer)
    A18 = Column(Integer)
    Q19 = Column(Integer)
    A19 = Column(Integer)
    Q20 = Column(Integer)
    A20 = Column(Integer)
    Q21 = Column(Integer)
    A21 = Column(Integer)
    Q22 = Column(Integer)
    A22 = Column(Integer)
    Q23 = Column(Integer)
    A23 = Column(Integer)
    Q24 = Column(Integer)
    A24 = Column(Integer)
    Q25 = Column(Integer)
    A25 = Column(Integer)
    Q26 = Column(Integer)
    A26 = Column(Integer)
	
def main():

    engine = create_engine('sqlite:///./data.db')    
    Base.metadata.create_all(engine)
    
if __name__ == '__main__':
    main()
    print('Done :)')
