# file typesystem/base.py:184-185
# lines [185]
# branches []

import pytest
from typesystem.base import BaseError

def test_base_error_getitem():
    class CustomError(BaseError):
        def __init__(self, message_dict):
            self._message_dict = message_dict

    error_message = {"key1": "value1", "key2": "value2"}
    error_instance = CustomError(error_message)

    assert error_instance["key1"] == "value1"
    assert error_instance["key2"] == "value2"

    with pytest.raises(KeyError):
        _ = error_instance["key3"]
