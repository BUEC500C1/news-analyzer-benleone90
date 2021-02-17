from flask import Flask
from flask_restful import Api, Resource
import os

app = Flask(__name__)
api = Api(app)


class fileUpload(Resource):
    def post(self, file):  # CREATE
        pass

    def get(self, file):  # READ
        pass

    def put(self, file):  # UPDATE
        pass

    def delete(self, file):  # DELETE
        pass


api.add_resource(fileUpload, "/file/<string:file>")

if __name__ == "__main__":
    app.run(debug=True)
