from flask import Flask, request
from flask_restful import Resource, Api
from google.cloud import language_v1

app = Flask(__name__)
api = Api(app)
client = language_v1.LanguageServiceClient()

testing = u"Hello, World!"  # Unicode stringl
document = language_v1.Document(
    content=testing, type=language_v1.Document.Type.PLAIN_TEXT)


class test(Resource):
    def get(self, text):
        return text


api.add_resource(test, "/api/<string:text>")

if __name__ == '__main__':
    app.run(debug=True)
