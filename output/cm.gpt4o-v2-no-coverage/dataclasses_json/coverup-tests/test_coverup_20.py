# file: dataclasses_json/mm.py:29-46
# asked: {"lines": [31, 32, 34, 35, 37, 40, 41, 43, 44, 46], "branches": [[31, 32], [31, 34], [34, 35], [34, 37], [40, 41], [40, 43], [43, 44], [43, 46]]}
# gained: {"lines": [31, 32, 34, 35, 37, 40, 41, 43, 44, 46], "branches": [[31, 32], [31, 34], [34, 35], [34, 37], [40, 41], [40, 43], [43, 44], [43, 46]]}

import pytest
from marshmallow.exceptions import ValidationError
from dataclasses_json.mm import _TimestampField
from datetime import datetime, timezone

def test_serialize_with_value():
    field = _TimestampField()
    dt = datetime(2023, 1, 1, tzinfo=timezone.utc)
    result = field._serialize(dt, None, None)
    assert result == dt.timestamp()

def test_serialize_without_value_not_required():
    field = _TimestampField(required=False)
    result = field._serialize(None, None, None)
    assert result is None

def test_serialize_without_value_required():
    field = _TimestampField(required=True)
    with pytest.raises(ValidationError) as excinfo:
        field._serialize(None, None, None)
    assert str(excinfo.value) == "Missing data for required field."

def test_deserialize_with_value():
    field = _TimestampField()
    timestamp = 1672531200.0  # Corresponds to 2023-01-01 00:00:00 UTC
    result = field._deserialize(timestamp, None, None)
    assert result == datetime.fromtimestamp(timestamp, tz=timezone.utc)

def test_deserialize_without_value_not_required():
    field = _TimestampField(required=False)
    result = field._deserialize(None, None, None)
    assert result is None

def test_deserialize_without_value_required():
    field = _TimestampField(required=True)
    with pytest.raises(ValidationError) as excinfo:
        field._deserialize(None, None, None)
    assert str(excinfo.value) == "Missing data for required field."
