from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text, create_engine, ForeignKey
from flask_login import UserMixin

Base = declarative_base()

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
    password_hash = Column(String(255), nullable=False)

class BLOCK(Base):
    __tablename__ = 'BLOCK'
    
    ID = Column(Integer, primary_key=True)
    BLOCK = Column(String(9))
    START_DATE = Column(DateTime)
    END_DATE = Column(DateTime)
    AY = Column(String(9))
    
class DEPARTMENT(Base):
    __tablename__ = 'DEPARTMENT'
    
    DEPARTMENT_ID = Column(Integer, primary_key=True)
    DEPARTMENT = Column(Text)
    DEPARTMENT_ABBR = Column(String(10))
    
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
    BLOCK = Column(Integer)
    DEPARTMENT = Column(Integer)
    CALENDAR_YEAR = Column(String(9))
    LOCATION = Column(Integer)
    
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
	
def main():

    engine = create_engine('sqlite:///./data.db')    
    Base.metadata.create_all(engine)
    
if __name__ == '__main__':
    main()
    print('Done :)')
