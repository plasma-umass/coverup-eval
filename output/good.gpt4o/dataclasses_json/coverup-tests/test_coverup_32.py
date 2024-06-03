# file dataclasses_json/mm.py:49-66
# lines [51, 52, 54, 55, 57, 60, 61, 63, 64, 66]
# branches ['51->52', '51->54', '54->55', '54->57', '60->61', '60->63', '63->64', '63->66']

import pytest
from datetime import datetime
from marshmallow import fields, ValidationError
from dataclasses_json.mm import _IsoField

def test_iso_field_serialize_with_value():
    field = _IsoField()
    value = datetime(2023, 10, 1, 12, 0, 0)
    result = field._serialize(value, None, None)
    assert result == "2023-10-01T12:00:00"

def test_iso_field_serialize_without_value_not_required():
    field = _IsoField(required=False)
    result = field._serialize(None, None, None)
    assert result is None

def test_iso_field_serialize_without_value_required():
    field = _IsoField(required=True)
    with pytest.raises(ValidationError):
        field._serialize(None, None, None)

def test_iso_field_deserialize_with_value():
    field = _IsoField()
    value = "2023-10-01T12:00:00"
    result = field._deserialize(value, None, None)
    assert result == datetime(2023, 10, 1, 12, 0, 0)

def test_iso_field_deserialize_without_value_not_required():
    field = _IsoField(required=False)
    result = field._deserialize(None, None, None)
    assert result is None

def test_iso_field_deserialize_without_value_required():
    field = _IsoField(required=True)
    with pytest.raises(ValidationError):
        field._deserialize(None, None, None)
