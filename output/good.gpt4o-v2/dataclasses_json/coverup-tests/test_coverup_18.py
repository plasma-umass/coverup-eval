# file: dataclasses_json/mm.py:29-46
# asked: {"lines": [29, 30, 31, 32, 34, 35, 37, 39, 40, 41, 43, 44, 46], "branches": [[31, 32], [31, 34], [34, 35], [34, 37], [40, 41], [40, 43], [43, 44], [43, 46]]}
# gained: {"lines": [29, 30, 31, 32, 34, 35, 37, 39, 40, 41, 43, 44, 46], "branches": [[31, 32], [31, 34], [34, 35], [34, 37], [40, 41], [40, 43], [43, 44], [43, 46]]}

import pytest
from marshmallow.exceptions import ValidationError
from datetime import datetime, timezone, timedelta
from dataclasses_json.mm import _TimestampField

def test_serialize_with_value():
    field = _TimestampField()
    value = datetime(2023, 1, 1, tzinfo=timezone.utc)
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

def test_deserialize_with_value(mocker):
    field = _TimestampField()
    value = 1672531200  # Equivalent to datetime(2023, 1, 1).timestamp()
    mocker.patch('dataclasses_json.utils._timestamp_to_dt_aware', return_value=datetime(2023, 1, 1, tzinfo=timezone.utc))
    result = field._deserialize(value, None, None)
    assert result == datetime(2023, 1, 1, tzinfo=timezone.utc)

def test_deserialize_without_value_not_required():
    field = _TimestampField(required=False)
    result = field._deserialize(None, None, None)
    assert result is None

def test_deserialize_without_value_required():
    field = _TimestampField(required=True)
    with pytest.raises(ValidationError):
        field._deserialize(None, None, None)
