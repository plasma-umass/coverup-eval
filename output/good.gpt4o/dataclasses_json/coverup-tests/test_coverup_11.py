# file dataclasses_json/mm.py:29-46
# lines [29, 30, 31, 32, 34, 35, 37, 39, 40, 41, 43, 44, 46]
# branches ['31->32', '31->34', '34->35', '34->37', '40->41', '40->43', '43->44', '43->46']

import pytest
from marshmallow import fields, ValidationError
from datetime import datetime, timezone

# Assuming _timestamp_to_dt_aware is defined somewhere in dataclasses_json.mm
from dataclasses_json.mm import _timestamp_to_dt_aware

class _TimestampField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is not None:
            return value.timestamp()
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

    def _deserialize(self, value, attr, data, **kwargs):
        if value is not None:
            return _timestamp_to_dt_aware(value)
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

def test_timestamp_field_serialize():
    field = _TimestampField(required=True)
    dt = datetime(2023, 1, 1, tzinfo=timezone.utc)
    assert field._serialize(dt, None, None) == dt.timestamp()

    field_not_required = _TimestampField(required=False)
    assert field_not_required._serialize(None, None, None) is None

    with pytest.raises(ValidationError):
        field._serialize(None, None, None)

def test_timestamp_field_deserialize(mocker):
    field = _TimestampField(required=True)
    timestamp = 1672531200  # Corresponds to 2023-01-01 00:00:00 UTC
    mocker.patch('dataclasses_json.mm._timestamp_to_dt_aware', return_value=datetime.fromtimestamp(timestamp, tz=timezone.utc))
    assert field._deserialize(timestamp, None, None) == datetime.fromtimestamp(timestamp, tz=timezone.utc)

    field_not_required = _TimestampField(required=False)
    assert field_not_required._deserialize(None, None, None) is None

    with pytest.raises(ValidationError):
        field._deserialize(None, None, None)
