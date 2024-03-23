# file typesystem/fields.py:24-48
# lines [24, 27, 28, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 43, 47, 48]
# branches ['35->36', '35->38', '38->39', '38->41']

import pytest
from typesystem.fields import Field, NO_DEFAULT

def test_field_initialization_with_default():
    field = Field(default="default_value")
    assert field.default == "default_value"

def test_field_initialization_without_default():
    field = Field()
    assert not hasattr(field, 'default')

def test_field_initialization_with_allow_null():
    field = Field(allow_null=True)
    assert field.allow_null is True
    assert field.default is None

def test_field_initialization_with_allow_null_and_default():
    field = Field(allow_null=True, default="default_value")
    assert field.allow_null is True
    assert field.default == "default_value"

def test_field_initialization_with_title_and_description():
    field = Field(title="Test Title", description="Test Description")
    assert field.title == "Test Title"
    assert field.description == "Test Description"

def test_field_creation_counter():
    initial_counter = Field._creation_counter
    field1 = Field()
    field2 = Field()
    assert field1._creation_counter == initial_counter
    assert field2._creation_counter == initial_counter + 1
    Field._creation_counter = initial_counter  # Reset the counter after the test

@pytest.fixture(autouse=True)
def reset_field_creation_counter():
    # Store the original creation counter before each test
    original_counter = Field._creation_counter
    yield
    # Reset the creation counter after each test
    Field._creation_counter = original_counter
