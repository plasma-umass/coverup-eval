# file typesystem/fields.py:65-66
# lines [65, 66]
# branches []

import pytest
from typesystem.fields import Field

def test_field_has_default():
    field_with_default = Field()
    field_with_default.default = 'some_default_value'
    field_without_default = Field()

    assert field_with_default.has_default() is True
    assert field_without_default.has_default() is False
