# file typesystem/base.py:181-182
# lines [181, 182]
# branches []

import pytest
from typesystem.base import BaseError

def test_base_error_len():
    class TestError(BaseError):
        def __init__(self, message_dict):
            self._message_dict = message_dict

    message_dict = {'field1': 'error1', 'field2': 'error2'}
    error = TestError(message_dict)
    assert len(error) == len(message_dict), "BaseError __len__ should return the length of _message_dict"
