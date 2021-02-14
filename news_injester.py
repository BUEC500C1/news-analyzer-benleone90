from flask import Flask
from flask_restful import Api, Resource
from newsapi import NewsApiClient
import os

app = Flask(__name__)
api = Api(app)
news_key = os.environ.get("NEWS_KEY")
newsapi = NewsApiClient(api_key=news_key)


class newsInjest(Resource):
    def get(self):
        top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                                  language='en')
        return top_headlines


api.add_resource(newsInjest, "/")

if __name__ == '__main__':
    app.run(debug=True)
