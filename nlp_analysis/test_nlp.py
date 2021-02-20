import pytest
import requests
from nlp_analysis import analyzeSentiment

# Check on how to deply envvar for GitHub Actions with NLP


def test_status():
    response = requests.get('http://127.0.0.1:5000/nlp/Hello World!')
    assert response.status_code == 200
