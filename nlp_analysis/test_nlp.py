import pytest
import requests
from nlp_analysis import analyzeSent

# Check on how to deply envvar for GitHub Actions with NLP


def test_status():
    response = requests.get('http://127.0.0.1:5000/nlp/bitcoin')
    assert response.status_code == 200
