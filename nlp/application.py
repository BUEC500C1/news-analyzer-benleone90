from flask import Flask, request, render_template, jsonify
from google.cloud import language_v1
import os

# template_dir = os.path.abspath('./')
app = Flask(__name__)
client = language_v1.LanguageServiceClient()


@app.route("/")
def index():
    return render_template("nlp.html")


@app.route("/nlp", methods=['GET', 'POST'])
def nlp():
    text = request.form.get('content')
    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(
        request={'document': document}).document_sentiment
    # app.logger.info('Test message')
    response = {'text': text, 'score': sentiment.score,
                'magnitude': sentiment.magnitude}
    return render_template("nlp.html", response=response)


if __name__ == '__main__':
    app.run(debug=True)
