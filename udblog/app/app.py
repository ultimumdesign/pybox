from flask import Flask
from flask_restful import Resource, Api
import os
from flask import Markup
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# Configure MySQL connection.
db = SQLAlchemy()
db_uri = 'mysql://root:supersecure@db/information_schema'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
