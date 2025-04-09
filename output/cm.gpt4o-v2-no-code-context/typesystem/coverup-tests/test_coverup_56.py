# file: typesystem/fields.py:402-444
# asked: {"lines": [417, 418], "branches": [[416, 417]]}
# gained: {"lines": [417, 418], "branches": [[416, 417]]}

import pytest
from typesystem.fields import Field, Object

class DummyField(Field):
    pass

def test_object_with_field_as_properties():
    dummy_field = DummyField()
    obj = Object(properties=dummy_field)
    
    assert obj.additional_properties == dummy_field
    assert obj.properties == {}

def test_object_with_dict_as_properties():
    dummy_field = DummyField()
    obj = Object(properties={"key": dummy_field})
    
    assert obj.additional_properties is True
    assert obj.properties == {"key": dummy_field}

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Any necessary cleanup can be done here
    yield
    # Cleanup code here if needed
