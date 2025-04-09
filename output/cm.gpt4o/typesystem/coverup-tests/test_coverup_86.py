# file typesystem/base.py:178-179
# lines [179]
# branches []

import pytest
from typesystem.base import BaseError

def test_baseerror_iter():
    class CustomError(BaseError):
        def __init__(self, message_dict):
            self._message_dict = message_dict

    error_instance = CustomError({"key1": "value1", "key2": "value2"})
    iterator = iter(error_instance)
    
    assert next(iterator) == "key1"
    assert next(iterator) == "key2"
    
    with pytest.raises(StopIteration):
        next(iterator)
