# file tornado/log.py:74-78
# lines [77, 78]
# branches []

import pytest
from unittest import mock
from tornado.log import _safe_unicode

def test_safe_unicode_with_unicode_decode_error(mocker):
    # Mock the _unicode function to raise a UnicodeDecodeError
    mock_unicode = mocker.patch('tornado.log._unicode', side_effect=UnicodeDecodeError("codec", b"", 0, 1, "reason"))

    # Test input that will trigger the UnicodeDecodeError
    test_input = b'\x80'

    # Call the function and assert the expected output
    result = _safe_unicode(test_input)
    assert result == repr(test_input)

    # Ensure the mock was called
    mock_unicode.assert_called_once_with(test_input)
