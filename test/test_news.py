import pytest
import requests
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from news.application import all_articles

def test_news_injest():
    response = requests.get("http://127.0.0.1:5000/news/bitcoin")
    assert response.status_code == 200
