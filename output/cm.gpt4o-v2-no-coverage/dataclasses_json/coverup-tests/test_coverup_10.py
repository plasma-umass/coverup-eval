# file: dataclasses_json/core.py:90-93
# asked: {"lines": [90, 91, 92, 93], "branches": [[91, 92], [91, 93]]}
# gained: {"lines": [90, 91, 92, 93], "branches": [[91, 92], [91, 93]]}

import pytest
from dataclasses_json.core import _encode_json_type, _ExtendedEncoder, Json

def test_encode_json_type_with_json_args():
    # Test when value is an instance of Json.__args__
    value = 123  # int is part of Json.__args__
    result = _encode_json_type(value)
    assert result == value

def test_encode_json_type_with_non_json_args(mocker):
    # Test when value is not an instance of Json.__args__
    value = object()  # object is not part of Json.__args__
    mock_default = mocker.patch.object(_ExtendedEncoder, 'default', side_effect=lambda x: "encoded")
    result = _encode_json_type(value, default=mock_default)
    mock_default.assert_called_once_with(value)
    assert result == "encoded"
