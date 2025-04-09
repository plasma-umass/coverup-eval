# file: typesystem/fields.py:24-48
# asked: {"lines": [24, 27, 28, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 43, 47, 48], "branches": [[35, 36], [35, 38], [38, 39], [38, 41]]}
# gained: {"lines": [24, 27, 28, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 43, 47, 48], "branches": [[35, 36], [35, 38], [38, 39], [38, 41]]}

import pytest
from typesystem.fields import Field, NO_DEFAULT

@pytest.fixture(autouse=True)
def reset_creation_counter():
    original_counter = Field._creation_counter
    Field._creation_counter = 0
    yield
    Field._creation_counter = original_counter

def test_field_initialization_with_defaults():
    field = Field()
    assert field.title == ""
    assert field.description == ""
    assert not hasattr(field, 'default')
    assert field.allow_null is False
    assert field._creation_counter == 0

def test_field_initialization_with_custom_values():
    field = Field(title="Test Title", description="Test Description", default="default_value", allow_null=True)
    assert field.title == "Test Title"
    assert field.description == "Test Description"
    assert field.default == "default_value"
    assert field.allow_null is True
    assert field._creation_counter == 0

def test_field_initialization_with_allow_null_and_no_default():
    field = Field(allow_null=True)
    assert field.title == ""
    assert field.description == ""
    assert field.default is None
    assert field.allow_null is True
    assert field._creation_counter == 0

def test_field_creation_counter_increments():
    field1 = Field()
    field2 = Field()
    assert field1._creation_counter == 0
    assert field2._creation_counter == 1
