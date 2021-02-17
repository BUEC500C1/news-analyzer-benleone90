from flask import Flask
from flask_restful import Api, Resource
from newsapi import NewsApiClient
import os

app = Flask(__name__)
api = Api(app)
news_key = os.environ.get("NEWS_KEY")
newsapi = NewsApiClient(api_key=news_key)


class newsInjest(Resource):
    def get(self, query):
        all_articles = newsapi.get_everything(
            q=query, language='en', sort_by='relevancy')
        return all_articles


api.add_resource(newsInjest, "/news/<string:query>")

if __name__ == '__main__':
    app.run(debug=True)
