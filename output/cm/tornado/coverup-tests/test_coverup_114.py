# file tornado/options.py:121-124
# lines [121, 122, 124]
# branches []

import pytest
from tornado.options import Error

def test_tornado_options_error():
    # Test that the Error class can be instantiated and is of the correct type
    try:
        raise Error("This is a test error")
    except Error as e:
        assert isinstance(e, Error)
        assert str(e) == "This is a test error"
