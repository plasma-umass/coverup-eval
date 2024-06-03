# file mimesis/providers/internet.py:183-218
# lines [183, 184, 185, 186, 187, 202, 204, 205, 207, 209, 211, 212, 213, 214, 215, 216, 217, 218]
# branches ['204->205', '204->207', '211->212', '211->218']

import pytest
import urllib.error
from unittest.mock import patch, MagicMock
from mimesis.providers.internet import Internet

@pytest.fixture
def internet_provider():
    return Internet()

def test_stock_image_url(internet_provider):
    url = internet_provider.stock_image(width=800, height=600, keywords=['nature', 'water'])
    assert url == 'https://source.unsplash.com/800x600?nature,water'

def test_stock_image_no_keywords(internet_provider):
    url = internet_provider.stock_image(width=800, height=600)
    assert url == 'https://source.unsplash.com/800x600?'

def test_stock_image_writable_success(internet_provider):
    mock_response = MagicMock()
    mock_response.read.return_value = b'image_bytes'
    with patch('urllib.request.urlopen', return_value=mock_response):
        image_bytes = internet_provider.stock_image(width=800, height=600, writable=True)
        assert image_bytes == b'image_bytes'

def test_stock_image_writable_failure(internet_provider):
    with patch('urllib.request.urlopen', side_effect=urllib.error.URLError('No connection')):
        with pytest.raises(urllib.error.URLError, match='Required an active HTTP connection'):
            internet_provider.stock_image(width=800, height=600, writable=True)
