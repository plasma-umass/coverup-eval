# file typesystem/fields.py:50-51
# lines [50, 51]
# branches []

import pytest
from typesystem.fields import Field

def test_field_validate_not_implemented():
    field = Field()
    with pytest.raises(NotImplementedError):
        field.validate("test_value", strict=True)
