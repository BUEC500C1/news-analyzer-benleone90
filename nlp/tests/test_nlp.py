from nlp.application import analyzeSentiment
import pytest
import requests
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# def test_status():
#     response = requests.get('http://127.0.0.1:5000/nlp/sentiment/Hello World!')
#     assert response.status_code == 200


def test_sentiment():
    response = analyzeSentiment('Hello world!')
    assert type(response) is dict