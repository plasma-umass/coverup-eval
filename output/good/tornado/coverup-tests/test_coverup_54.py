# file tornado/util.py:190-205
# lines [190, 200, 201, 202, 203, 205]
# branches ['200->201', '200->202', '202->203', '202->205']

import pytest
from tornado.util import errno_from_exception

class MockErrnoException(Exception):
    errno = 123

class MockArgsException(Exception):
    def __init__(self, arg):
        super().__init__(arg)

def test_errno_from_exception_with_errno():
    e = MockErrnoException()
    assert errno_from_exception(e) == 123

def test_errno_from_exception_with_args():
    e = MockArgsException(456)
    assert errno_from_exception(e) == 456

def test_errno_from_exception_without_errno_or_args():
    e = Exception()
    assert errno_from_exception(e) is None
