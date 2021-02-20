import pytest
import requests
from news_injester import all_articles


def test_news_injest():
    response = requests.get("http://127.0.0.1:5000/news/bitcoin")
    assert response.status_code == 200
