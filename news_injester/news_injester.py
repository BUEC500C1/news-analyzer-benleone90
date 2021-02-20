from flask import Flask, request, logging
from newsapi import NewsApiClient
import os

app = Flask(__name__)
news_key = os.environ.get("NEWS_KEY")
newsapi = NewsApiClient(api_key=news_key)


@app.route('/news/<query>', methods=['GET'])
def all_articles(query=None):
    all_articles = newsapi.get_everything(
        q=query, language='en', sort_by='relevancy')
    return all_articles


if __name__ == '__main__':
    app.run(debug=True)
