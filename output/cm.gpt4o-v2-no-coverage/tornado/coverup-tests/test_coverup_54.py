# file: tornado/util.py:170-187
# asked: {"lines": [170, 179, 180, 181, 183, 187], "branches": [[180, 181], [180, 183]]}
# gained: {"lines": [170, 179, 180, 181, 183, 187], "branches": [[180, 181], [180, 183]]}

import pytest

from tornado.util import raise_exc_info

def test_raise_exc_info_with_exception():
    exc_info = (None, ValueError("test error"), None)
    with pytest.raises(ValueError, match="test error"):
        raise_exc_info(exc_info)

def test_raise_exc_info_without_exception():
    exc_info = (None, None, None)
    with pytest.raises(TypeError, match="raise_exc_info called with no exception"):
        raise_exc_info(exc_info)
