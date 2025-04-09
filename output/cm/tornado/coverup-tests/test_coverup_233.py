# file tornado/log.py:74-78
# lines [77, 78]
# branches []

import pytest
from tornado.log import _safe_unicode

def test_safe_unicode_with_unicode_decode_error(mocker):
    # Mock the _unicode function to raise a UnicodeDecodeError
    mocker.patch('tornado.log._unicode', side_effect=UnicodeDecodeError('utf-8', b'', 0, 1, 'invalid start byte'))

    # Create a byte string that would cause a UnicodeDecodeError
    invalid_byte_string = b'\xff'

    # Call _safe_unicode with the invalid byte string
    result = _safe_unicode(invalid_byte_string)

    # Assert that the result is the repr of the invalid byte string
    assert result == repr(invalid_byte_string)

    # Cleanup is handled by pytest-mock through its patching mechanism
