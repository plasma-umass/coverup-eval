# file: tornado/options.py:121-124
# asked: {"lines": [121, 122, 124], "branches": []}
# gained: {"lines": [121, 122, 124], "branches": []}

import pytest
from tornado.options import Error

def test_error_exception():
    with pytest.raises(Error):
        raise Error("This is a test error")
