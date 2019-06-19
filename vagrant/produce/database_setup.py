import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String 
form sqalalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Produce(Base):

	__tablename__ = 'produce'
	
	id = Column(Integer, primary_key=True)
	name