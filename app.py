#app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resourse, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resourse):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
