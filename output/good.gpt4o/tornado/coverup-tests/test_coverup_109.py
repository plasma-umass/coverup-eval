# file tornado/options.py:121-124
# lines [121, 122, 124]
# branches []

import pytest
from tornado.options import Error

def test_error_exception():
    with pytest.raises(Error) as excinfo:
        raise Error("This is a test error")
    assert str(excinfo.value) == "This is a test error"
