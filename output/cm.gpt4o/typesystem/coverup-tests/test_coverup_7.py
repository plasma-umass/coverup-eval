# file typesystem/fields.py:24-48
# lines [24, 27, 28, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 43, 47, 48]
# branches ['35->36', '35->38', '38->39', '38->41']

import pytest
from typesystem.fields import Field, NO_DEFAULT

def test_field_initialization():
    # Test with all default parameters
    field = Field()
    assert field.title == ""
    assert field.description == ""
    assert field.allow_null == False
    assert not hasattr(field, 'default')

    # Test with custom title and description
    field = Field(title="Test Title", description="Test Description")
    assert field.title == "Test Title"
    assert field.description == "Test Description"

    # Test with default value
    field = Field(default="default_value")
    assert field.default == "default_value"

    # Test with allow_null and default is NO_DEFAULT
    field = Field(allow_null=True)
    assert field.allow_null == True
    assert field.default is None

    # Test with allow_null and default is not NO_DEFAULT
    field = Field(allow_null=True, default="default_value")
    assert field.allow_null == True
    assert field.default == "default_value"

    # Test creation counter
    initial_counter = Field._creation_counter
    field1 = Field()
    field2 = Field()
    assert field1._creation_counter == initial_counter
    assert field2._creation_counter == initial_counter + 1

@pytest.fixture(autouse=True)
def reset_creation_counter():
    # Save the original counter value
    original_counter = Field._creation_counter
    yield
    # Reset the counter after each test
    Field._creation_counter = original_counter
