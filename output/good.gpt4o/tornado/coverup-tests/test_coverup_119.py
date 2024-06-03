# file tornado/escape.py:106-108
# lines [106, 107, 108]
# branches []

import pytest
from tornado.escape import url_unescape

def test_url_unescape_bytes():
    # Test the url_unescape function with bytes input and encoding set to None
    input_value = b'hello%20world'
    expected_output = b'hello world'
    result = url_unescape(input_value, encoding=None, plus=True)
    assert result == expected_output

    input_value = b'hello+world'
    expected_output = b'hello world'
    result = url_unescape(input_value, encoding=None, plus=True)
    assert result == expected_output

    input_value = b'hello+world'
    expected_output = b'hello+world'
    result = url_unescape(input_value, encoding=None, plus=False)
    assert result == expected_output
