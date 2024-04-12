# file tornado/auth.py:1170-1173
# lines [1170, 1171, 1172, 1173]
# branches ['1171->1172', '1171->1173']

import pytest
from tornado.auth import _oauth_escape
from tornado.util import unicode_type

def test_oauth_escape_with_unicode(mocker):
    # Mocking urllib.parse.quote to ensure it is called with the correct parameters
    mock_quote = mocker.patch('urllib.parse.quote', return_value='mocked_value')

    # Test with a unicode string
    input_val = u"test\u00e9"  # Unicode string with an accented 'e'
    expected_val = b"test\xc3\xa9"  # UTF-8 encoded version of the above string

    # Call the function with a unicode string
    result = _oauth_escape(input_val)

    # Check that the result is as expected
    assert result == 'mocked_value'
    # Check that urllib.parse.quote was called with the encoded string and safe parameter
    mock_quote.assert_called_once_with(expected_val, safe="~")

def test_oauth_escape_with_bytes(mocker):
    # Mocking urllib.parse.quote to ensure it is called with the correct parameters
    mock_quote = mocker.patch('urllib.parse.quote', return_value='mocked_value')

    # Test with a bytes object
    input_val = b"test"
    expected_val = b"test"  # Bytes should stay the same

    # Call the function with a bytes object
    result = _oauth_escape(input_val)

    # Check that the result is as expected
    assert result == 'mocked_value'
    # Check that urllib.parse.quote was called with the bytes object and safe parameter
    mock_quote.assert_called_once_with(expected_val, safe="~")
