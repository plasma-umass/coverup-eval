# file tornado/escape.py:219-229
# lines [219, 225, 226, 227, 228, 229]
# branches ['225->226', '225->227', '227->228', '227->229']

import pytest
from tornado.escape import to_unicode

_TO_UNICODE_TYPES = (str, type(None))

@pytest.mark.parametrize("input_value,expected", [
    (None, None),
    ("already_unicode", "already_unicode"),
    (b"byte_string", "byte_string"),
])
def test_to_unicode(input_value, expected):
    assert to_unicode(input_value) == expected

def test_to_unicode_with_non_string_or_bytes():
    with pytest.raises(TypeError):
        to_unicode(1234)  # This should raise a TypeError
