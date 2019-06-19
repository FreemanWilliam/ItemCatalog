import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String 
from sqlalchemy.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Produce(Base):

	__tablename__ = 'produce'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)

class ProduceItem(Base):

	__tablename__ = 'produce_item'
	
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	price = Column(String(8))
	type = Column(String(20))
	produce_id = Column(Integer, ForeignKey('produce.id'))
	produce = relationship(Produce)
	
engine = create_engine(
'sqlite:///producemenu.db')

Base.metadata.create_all(engine)