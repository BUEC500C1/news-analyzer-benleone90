from flask import Flask, request, render_template
from newsapi import NewsApiClient
import os

# template_dir = os.path.abspath('./')
app = Flask(__name__)
news_key = os.environ.get("NEWS_KEY")
newsapi = NewsApiClient(api_key=news_key)


@app.route('/')
def index():
    return render_template("news_injest.html")


@app.route('/news/<string:query>', methods=['GET'])
def all_articles(query):
    all_articles = newsapi.get_everything(
        q=query, language='en', sort_by='relevancy')
    #app.logger.info('Test message')
    return render_template("news_injest.html", results=all_articles)


if __name__ == '__main__':
    app.run(debug=True)
