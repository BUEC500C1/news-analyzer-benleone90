from flask import Flask, request, render_template, url_for, jsonify
from newsapi import NewsApiClient
import os

# template_dir = os.path.abspath('./')
application = Flask(__name__)
news_key = os.environ.get("NEWS_KEY")
newsapi = NewsApiClient(api_key=news_key)


@application.route('/')
def index():
    return render_template("news.html")


@application.route('/news', methods=['POST'])
def news():
    query = request.form.get('query')
    results = newsapi.get_everything(
        q=query, language='en', sort_by='relevancy')
    #app.logger.info('Test message')
    return render_template("news.html", results=results)


if __name__ == '__main__':
    application.run(debug=True)
