from flask import Flask, request
from flask_restful import Resource, Api
from google.cloud import language_v1

app = Flask(__name__)
api = Api(app)
client = language_v1.LanguageServiceClient()

# text = u"Hello, World!"  # Unicode string


class analyzeSent(Resource):
    def get(self, text):
        document = language_v1.Document(
            content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(
            request={'document': document}).document_sentiment
        return {'text': text, 'score': sentiment.score, 'magnitude': sentiment.magnitude}


api.add_resource(analyzeSent, "/nlp/<string:text>")

if __name__ == '__main__':
    app.run(debug=True)
