# file mimesis/providers/internet.py:183-218
# lines [218]
# branches ['211->218']

import pytest
from mimesis.providers import Internet
from unittest.mock import patch
from urllib.error import URLError

def test_stock_image_writable_false():
    internet = Internet()
    # Test with writable=False, should return URL
    result = internet.stock_image(writable=False)
    assert isinstance(result, str)
    assert result.startswith('https://source.unsplash.com/')

def test_stock_image_writable_true():
    internet = Internet()
    # Test with writable=True, should raise URLError if no connection
    with patch('urllib.request.urlopen', side_effect=URLError('No connection')):
        with pytest.raises(URLError):
            _ = internet.stock_image(writable=True)
