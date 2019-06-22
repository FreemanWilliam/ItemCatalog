from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Produce, ProduceItem


@app.route('/')
@app.route('/produce')
def Produce():
	return "Hello World!!"

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port = 5000)