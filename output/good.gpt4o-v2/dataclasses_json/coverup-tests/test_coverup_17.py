# file: dataclasses_json/core.py:90-93
# asked: {"lines": [90, 91, 92, 93], "branches": [[91, 92], [91, 93]]}
# gained: {"lines": [90, 91, 92, 93], "branches": [[91, 92], [91, 93]]}

import pytest
from dataclasses_json.core import _encode_json_type, _ExtendedEncoder
from typing import Union

Json = Union[dict, list, str, int, float, bool, None]

def test_encode_json_type_with_json_args():
    # Test with a value that is an instance of Json.__args__
    assert _encode_json_type(123) == 123
    assert _encode_json_type("test") == "test"
    assert _encode_json_type(12.34) == 12.34
    assert _encode_json_type(True) == True
    assert _encode_json_type(None) == None
    assert _encode_json_type([1, 2, 3]) == [1, 2, 3]
    assert _encode_json_type({"key": "value"}) == {"key": "value"}

def test_encode_json_type_with_non_json_args(mocker):
    # Test with a value that is not an instance of Json.__args__
    mock_default = mocker.patch.object(_ExtendedEncoder, 'default', side_effect=lambda o: "encoded")
    class CustomType:
        pass

    custom_value = CustomType()
    assert _encode_json_type(custom_value, default=_ExtendedEncoder().default) == "encoded"
    mock_default.assert_called_once_with(custom_value)
