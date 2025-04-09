# file tornado/util.py:170-187
# lines [170, 179, 180, 181, 183, 187]
# branches ['180->181', '180->183']

import pytest
import sys
from tornado.util import raise_exc_info

def test_raise_exc_info_with_exception():
    try:
        raise ValueError("Test exception")
    except ValueError:
        exc_info = sys.exc_info()

    with pytest.raises(ValueError) as exc_info_context:
        raise_exc_info(exc_info)
    assert str(exc_info_context.value) == "Test exception"

def test_raise_exc_info_with_no_exception():
    exc_info = (None, None, None)
    with pytest.raises(TypeError) as exc_info_context:
        raise_exc_info(exc_info)
    assert str(exc_info_context.value) == "raise_exc_info called with no exception"
