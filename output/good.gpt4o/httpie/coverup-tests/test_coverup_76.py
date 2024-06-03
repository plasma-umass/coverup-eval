# file httpie/output/processing.py:12-13
# lines [12, 13]
# branches []

import pytest
from httpie.output.processing import is_valid_mime

def test_is_valid_mime(mocker):
    # Test with a valid MIME type
    valid_mime = "text/html"
    assert is_valid_mime(valid_mime) is not None

    # Test with an invalid MIME type
    invalid_mime = "invalid_mime"
    assert is_valid_mime(invalid_mime) is None

    # Test with an empty string
    empty_mime = ""
    assert is_valid_mime(empty_mime) == ""

    # Test with None
    none_mime = None
    assert is_valid_mime(none_mime) is None
