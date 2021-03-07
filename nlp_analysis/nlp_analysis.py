from flask import Flask, render_template, jsonify
from google.cloud import language_v1
import os

# template_dir = os.path.abspath('./')
app = Flask(__name__)
client = language_v1.LanguageServiceClient()


@app.route("/")
def index():
    return render_template("nlp_analysis.html")


@app.route("/nlp/<text>")
def analyzeSentiment(text=None):
    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(
        request={'document': document}).document_sentiment
    # app.logger.info('Test message')
    content = {'text': text, 'score': sentiment.score,
               'magnitude': sentiment.magnitude}
    jsonify(content)
    return render_template("nlp_analysis", content=content)


if __name__ == '__main__':
    app.run(debug=True)
