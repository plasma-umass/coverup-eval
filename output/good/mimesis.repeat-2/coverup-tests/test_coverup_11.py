# file mimesis/providers/internet.py:183-218
# lines [183, 184, 185, 186, 187, 202, 204, 205, 207, 209, 211, 212, 213, 214, 215, 216, 217, 218]
# branches ['204->205', '204->207', '211->212', '211->218']

import pytest
from unittest.mock import patch
from mimesis.providers.internet import Internet
from urllib.error import URLError

@pytest.fixture
def mock_urlopen(mocker):
    mock = mocker.patch('urllib.request.urlopen')
    mock.return_value.read.return_value = b'image_data'
    return mock

def test_stock_image_writable_true_with_keywords(mock_urlopen):
    keywords = ['nature', 'water']
    result = Internet.stock_image(width=100, height=100, keywords=keywords, writable=True)
    assert result == b'image_data'
    mock_urlopen.assert_called_once()

def test_stock_image_writable_true_without_keywords(mock_urlopen):
    result = Internet.stock_image(width=100, height=100, writable=True)
    assert result == b'image_data'
    mock_urlopen.assert_called_once()

def test_stock_image_writable_true_urlopen_exception(mocker):
    mocker.patch('urllib.request.urlopen', side_effect=URLError('Test Error'))
    with pytest.raises(URLError):
        Internet.stock_image(width=100, height=100, writable=True)
