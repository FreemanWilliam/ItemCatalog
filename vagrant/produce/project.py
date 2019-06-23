from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Produce, ProduceItem

engine = create_engine('sqlite:///producemenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/produce')
def Produce():

	
	
	
	
		
		
	return ""

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port = 5000)