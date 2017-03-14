""" Creating a database and creating tables in it"""

from sqlalchemy import create_engine, PrimaryKey
from sqlalchemy import Column, Integer, String, VarChar
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///quiz_results.db', echo = True)
Base = declarative_base()

class User (Base):
	__tablename__ = "User Login Details"

	user_id = Column (Integer, Primary_key = True)
	user_name = Column (VarChar)
	user_email = Column (VarChar)
	user_password = Column (VarChar)

	def __init__(self, Name = user_name, Email = user_email, Password = user_password):
		self.name = Name
		self.email = Email
		self.password = Password

class Results (Base):
	__tablename__ = "Contains the results of the user"

	quiz_id = Column (Integer, Primary_key = True)
	quiz_name = Column (VarChar)
	results_quiz = Column (VarChar)

	def __init__ (self, Subject = quiz_name, Results = results_quiz):
		self.subject = Subject
		self.results_quiz = Results

Base.metadata.create_all(engine)
