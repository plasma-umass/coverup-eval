# file typesystem/fields.py:20-23
# lines [20, 21, 22]
# branches []

import pytest
from typesystem.fields import Field

def test_field_creation_counter():
    initial_counter = Field._creation_counter
    field1 = Field()
    field2 = Field()
    assert Field._creation_counter == initial_counter + 2, "Field creation counter did not increment correctly"
    # Cleanup: Reset the creation counter to its initial value after the test
    Field._creation_counter = initial_counter
