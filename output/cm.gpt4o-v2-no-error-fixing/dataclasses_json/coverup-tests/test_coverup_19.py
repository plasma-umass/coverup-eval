# file: dataclasses_json/mm.py:29-46
# asked: {"lines": [31, 32, 34, 35, 37, 40, 41, 43, 44, 46], "branches": [[31, 32], [31, 34], [34, 35], [34, 37], [40, 41], [40, 43], [43, 44], [43, 46]]}
# gained: {"lines": [31, 32, 34, 35, 37, 40, 41, 43, 44, 46], "branches": [[31, 32], [31, 34], [34, 35], [34, 37], [40, 41], [40, 43], [43, 44], [43, 46]]}

import pytest
from marshmallow.exceptions import ValidationError
from dataclasses_json.mm import _TimestampField
from datetime import datetime
from dataclasses_json.utils import _timestamp_to_dt_aware

def test_serialize_with_value():
    field = _TimestampField()
    value = datetime.now()
    result = field._serialize(value, None, None)
    assert result == value.timestamp()

def test_serialize_without_value_not_required():
    field = _TimestampField(required=False)
    result = field._serialize(None, None, None)
    assert result is None

def test_serialize_without_value_required():
    field = _TimestampField(required=True)
    with pytest.raises(ValidationError):
        field._serialize(None, None, None)

def test_deserialize_with_value():
    field = _TimestampField()
    value = datetime.now().timestamp()
    result = field._deserialize(value, None, None)
    assert result == _timestamp_to_dt_aware(value)

def test_deserialize_without_value_not_required():
    field = _TimestampField(required=False)
    result = field._deserialize(None, None, None)
    assert result is None

def test_deserialize_without_value_required():
    field = _TimestampField(required=True)
    with pytest.raises(ValidationError):
        field._deserialize(None, None, None)
