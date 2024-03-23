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
    error_instance = TestError(message_dict)
    assert len(error_instance) == len(message_dict), "Length of BaseError instance should match length of message_dict"
