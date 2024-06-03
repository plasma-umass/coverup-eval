# file tornado/util.py:170-187
# lines [170, 179, 180, 181, 183, 187]
# branches ['180->181', '180->183']

import pytest
import sys
import traceback
from types import TracebackType
from typing import Optional, Tuple

# Assuming the function raise_exc_info is imported from tornado.util
from tornado.util import raise_exc_info

def test_raise_exc_info_with_exception():
    class CustomException(Exception):
        pass

    exc_type, exc_value, exc_tb = None, None, None
    try:
        raise CustomException("Test exception")
    except CustomException:
        exc_type, exc_value, exc_tb = sys.exc_info()

    with pytest.raises(CustomException, match="Test exception"):
        raise_exc_info((exc_type, exc_value, exc_tb))

def test_raise_exc_info_without_exception():
    with pytest.raises(TypeError, match="raise_exc_info called with no exception"):
        raise_exc_info((None, None, None))
