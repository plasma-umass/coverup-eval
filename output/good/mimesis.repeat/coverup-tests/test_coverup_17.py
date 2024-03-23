# file mimesis/providers/internet.py:183-218
# lines [183, 184, 185, 186, 187, 202, 204, 205, 207, 209, 211, 212, 213, 214, 215, 216, 217, 218]
# branches ['204->205', '204->207', '211->212', '211->218']

import pytest
from mimesis.providers.internet import Internet
from unittest.mock import patch
import urllib.error


@pytest.fixture
def mock_urlopen(mocker):
    mock = mocker.patch('urllib.request.urlopen', autospec=True)
    mock.return_value.read.return_value = b'stock_image_data'
    return mock


def test_stock_image_writable_true_with_keywords(mock_urlopen):
    keywords = ['nature', 'tech']
    result = Internet.stock_image(width=800, height=600, keywords=keywords, writable=True)
    assert result == b'stock_image_data'
    mock_urlopen.assert_called_once()


def test_stock_image_writable_true_without_keywords(mock_urlopen):
    result = Internet.stock_image(width=800, height=600, writable=True)
    assert result == b'stock_image_data'
    mock_urlopen.assert_called_once()


def test_stock_image_writable_true_urlopen_error(mocker):
    mocker.patch('urllib.request.urlopen', side_effect=urllib.error.URLError('Test Error'))
    with pytest.raises(urllib.error.URLError):
        Internet.stock_image(width=800, height=600, writable=True)
