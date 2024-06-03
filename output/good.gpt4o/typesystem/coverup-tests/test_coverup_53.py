# file typesystem/fields.py:65-66
# lines [65, 66]
# branches []

import pytest
from typesystem.fields import Field

def test_field_has_default():
    # Create an instance of Field without a default attribute
    field = Field()
    assert not field.has_default(), "Field should not have a default attribute initially"

    # Dynamically add a default attribute to the instance
    field.default = "some_default_value"
    assert field.has_default(), "Field should have a default attribute after setting it"

    # Clean up by removing the default attribute
    del field.default
    assert not field.has_default(), "Field should not have a default attribute after deletion"
