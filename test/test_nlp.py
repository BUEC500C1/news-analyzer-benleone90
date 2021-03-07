import pytest
import requests
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from nlp_analysis.nlp_analysis import analyzeSentiment

# Check on how to deply envvar for GitHub Actions with NLP


def test_status():
    response = requests.get('http://127.0.0.1:5000/nlp/Hello World!')
    assert response.status_code == 200
