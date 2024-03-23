# file dataclasses_json/mm.py:49-66
# lines [49, 50, 51, 52, 54, 55, 57, 59, 60, 61, 63, 64, 66]
# branches ['51->52', '51->54', '54->55', '54->57', '60->61', '60->63', '63->64', '63->66']

import pytest
from marshmallow import ValidationError
from datetime import datetime

# Assuming the _IsoField class is defined in the dataclasses_json.mm module
from dataclasses_json.mm import _IsoField

@pytest.fixture
def iso_field_optional():
    return _IsoField(required=False)

@pytest.fixture
def iso_field_required():
    return _IsoField(required=True)

def test_iso_field_serialize_optional_with_none(iso_field_optional):
    assert iso_field_optional._serialize(None, None, None) is None

def test_iso_field_serialize_required_with_none(iso_field_required):
    with pytest.raises(ValidationError):
        iso_field_required._serialize(None, None, None)

def test_iso_field_deserialize_optional_with_none(iso_field_optional):
    assert iso_field_optional._deserialize(None, None, None) is None

def test_iso_field_deserialize_required_with_none(iso_field_required):
    with pytest.raises(ValidationError):
        iso_field_required._deserialize(None, None, None)

def test_iso_field_serialize_with_value(iso_field_optional):
    now = datetime.now()
    assert iso_field_optional._serialize(now, None, None) == now.isoformat()

def test_iso_field_deserialize_with_value(iso_field_optional):
    now = datetime.now()
    iso_str = now.isoformat()
    assert iso_field_optional._deserialize(iso_str, None, None) == now
