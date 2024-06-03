# file tornado/escape.py:219-229
# lines [219, 225, 226, 227, 228, 229]
# branches ['225->226', '225->227', '227->228', '227->229']

import pytest
from tornado.escape import to_unicode

def test_to_unicode():
    # Test with None
    assert to_unicode(None) is None

    # Test with unicode string
    assert to_unicode("test") == "test"

    # Test with bytes
    assert to_unicode(b"test") == "test"

    # Test with invalid type (int)
    with pytest.raises(TypeError, match="Expected bytes, unicode, or None; got <class 'int'>"):
        to_unicode(123)
