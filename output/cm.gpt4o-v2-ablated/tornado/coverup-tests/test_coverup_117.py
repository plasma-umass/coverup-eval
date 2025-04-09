# file: tornado/util.py:190-205
# asked: {"lines": [200, 201, 202, 203, 205], "branches": [[200, 201], [200, 202], [202, 203], [202, 205]]}
# gained: {"lines": [200, 201, 202, 203, 205], "branches": [[200, 201], [200, 202], [202, 203], [202, 205]]}

import pytest
import errno
from typing import Optional

# Assuming the function is imported from the module
from tornado.util import errno_from_exception

def test_errno_from_exception_with_errno_attribute():
    class CustomExceptionWithErrno(Exception):
        def __init__(self, errno):
            self.errno = errno

    e = CustomExceptionWithErrno(errno.EACCES)
    assert errno_from_exception(e) == errno.EACCES

def test_errno_from_exception_with_args():
    e = Exception(errno.EACCES, "Permission denied")
    assert errno_from_exception(e) == errno.EACCES

def test_errno_from_exception_with_no_args():
    e = Exception()
    assert errno_from_exception(e) is None

def test_errno_from_exception_with_non_errno_first_arg():
    e = Exception("Some error message", errno.EACCES)
    assert errno_from_exception(e) == "Some error message"

def test_errno_from_exception_with_empty_args():
    e = Exception()
    e.args = ()
    assert errno_from_exception(e) is None
