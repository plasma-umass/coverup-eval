# file: tornado/util.py:190-205
# asked: {"lines": [190, 200, 201, 202, 203, 205], "branches": [[200, 201], [200, 202], [202, 203], [202, 205]]}
# gained: {"lines": [190, 200, 201, 202, 203, 205], "branches": [[200, 201], [200, 202], [202, 203], [202, 205]]}

import pytest

from tornado.util import errno_from_exception

def test_errno_from_exception_with_errno_attribute():
    class CustomException(Exception):
        def __init__(self, errno):
            self.errno = errno

    e = CustomException(5)
    assert errno_from_exception(e) == 5

def test_errno_from_exception_with_args():
    e = Exception(10)
    assert errno_from_exception(e) == 10

def test_errno_from_exception_with_no_args():
    e = Exception()
    assert errno_from_exception(e) is None

def test_errno_from_exception_with_no_errno_and_no_args():
    class CustomException(Exception):
        pass

    e = CustomException()
    assert errno_from_exception(e) is None
