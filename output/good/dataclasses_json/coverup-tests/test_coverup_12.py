# file dataclasses_json/mm.py:29-46
# lines [29, 30, 31, 32, 34, 35, 37, 39, 40, 41, 43, 44, 46]
# branches ['31->32', '31->34', '34->35', '34->37', '40->41', '40->43', '43->44', '43->46']

import pytest
from marshmallow import ValidationError
from dataclasses_json.mm import _TimestampField
from datetime import datetime, timezone

def _timestamp_to_dt_aware(value):
    # Mock function to replace the original _timestamp_to_dt_aware
    return datetime.fromtimestamp(value, tz=timezone.utc)

@pytest.fixture
def mock_timestamp_to_dt_aware(mocker):
    mocker.patch('dataclasses_json.mm._timestamp_to_dt_aware', side_effect=_timestamp_to_dt_aware)

def test_timestamp_field_serialize_not_required():
    field = _TimestampField(required=False)
    assert field._serialize(None, None, None) is None

def test_timestamp_field_serialize_required():
    field = _TimestampField(required=True)
    with pytest.raises(ValidationError):
        field._serialize(None, None, None)

def test_timestamp_field_deserialize_not_required(mock_timestamp_to_dt_aware):
    field = _TimestampField(required=False)
    assert field._deserialize(None, None, None) is None

def test_timestamp_field_deserialize_required(mock_timestamp_to_dt_aware):
    field = _TimestampField(required=True)
    with pytest.raises(ValidationError):
        field._deserialize(None, None, None)

def test_timestamp_field_serialize_with_value():
    field = _TimestampField()
    now = datetime.now()
    assert field._serialize(now, None, None) == now.timestamp()

def test_timestamp_field_deserialize_with_value(mock_timestamp_to_dt_aware):
    field = _TimestampField()
    now = datetime.now()
    assert field._deserialize(now.timestamp(), None, None) == _timestamp_to_dt_aware(now.timestamp())
