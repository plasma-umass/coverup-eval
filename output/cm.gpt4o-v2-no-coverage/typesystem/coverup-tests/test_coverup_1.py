# file: typesystem/fields.py:24-48
# asked: {"lines": [24, 27, 28, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 43, 47, 48], "branches": [[35, 36], [35, 38], [38, 39], [38, 41]]}
# gained: {"lines": [24, 27, 28, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 43, 47, 48], "branches": [[35, 36], [35, 38], [38, 39], [38, 41]]}

import pytest
from typesystem.fields import Field, NO_DEFAULT

def test_field_initialization():
    # Test default initialization
    field = Field()
    assert field.title == ""
    assert field.description == ""
    assert not hasattr(field, 'default')
    assert field.allow_null == False

    # Test initialization with parameters
    field = Field(title="Test Title", description="Test Description", default=42, allow_null=True)
    assert field.title == "Test Title"
    assert field.description == "Test Description"
    assert field.default == 42
    assert field.allow_null == True

    # Test allow_null with NO_DEFAULT
    field = Field(allow_null=True)
    assert field.default is None

    # Test creation counter
    initial_counter = Field._creation_counter
    field1 = Field()
    field2 = Field()
    assert field1._creation_counter == initial_counter
    assert field2._creation_counter == initial_counter + 1

@pytest.fixture(autouse=True)
def reset_creation_counter():
    # Reset the creation counter before each test to avoid state pollution
    Field._creation_counter = 0
