# file dataclasses_json/mm.py:29-46
# lines [31, 32, 34, 35, 37, 40, 41, 43, 44, 46]
# branches ['31->32', '31->34', '34->35', '34->37', '40->41', '40->43', '43->44', '43->46']

import pytest
from dataclasses_json.mm import _TimestampField
from marshmallow import ValidationError
from unittest.mock import Mock
import datetime

def test_timestamp_field_serialize():
    field = _TimestampField(required=True)
    value = datetime.datetime(2023, 1, 1, 12, 0, 0)
    assert field._serialize(value, None, None) == value.timestamp()

    field = _TimestampField(required=False)
    assert field._serialize(None, None, None) is None

    field = _TimestampField(required=True)
    with pytest.raises(ValidationError):
        field._serialize(None, None, None)

def test_timestamp_field_deserialize(mocker):
    mocker.patch('dataclasses_json.mm._timestamp_to_dt_aware', return_value='mocked_value')
    field = _TimestampField(required=True)
    value = 1672560000  # Corresponds to 2023-01-01 12:00:00
    assert field._deserialize(value, None, None) == 'mocked_value'

    field = _TimestampField(required=False)
    assert field._deserialize(None, None, None) is None

    field = _TimestampField(required=True)
    with pytest.raises(ValidationError):
        field._deserialize(None, None, None)
