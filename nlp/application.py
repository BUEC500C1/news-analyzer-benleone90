from flask import Flask, request
from google.cloud import language_v1

application = Flask(__name__)
client = language_v1.LanguageServiceClient()


@application.route('/nlp/sentiment/<text>')
def analyzeSentiment(text=None):
    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(
        request={'document': document}).document_sentiment
    return {'text': text, 'score': response.score, 'magnitude': response.magnitude, 'language': response.language}


if __name__ == '__main__':
    application.run(debug=True)
