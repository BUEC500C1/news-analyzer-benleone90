from flask import Flask, request
from google.cloud import language_v1

app = Flask(__name__)
client = language_v1.LanguageServiceClient()


@app.route("/nlp/<text>")
def analyzeSentiment(text=None):
    app.logger.info('Test message')
    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(
        request={'document': document}).document_sentiment
    return {'text': text, 'score': sentiment.score, 'magnitude': sentiment.magnitude}


if __name__ == '__main__':
    app.run(debug=True)
