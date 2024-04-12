# file typesystem/fields.py:50-51
# lines [50, 51]
# branches []

import pytest
from typesystem.fields import Field

class DummyField(Field):
    pass

def test_field_validate_not_implemented():
    dummy_field = DummyField()
    with pytest.raises(NotImplementedError):
        dummy_field.validate(None)
