# file mimesis/exceptions.py:70-74
# lines [70, 71, 73, 74]
# branches []

import pytest
from mimesis.exceptions import UndefinedField

def test_undefined_field_exception():
    with pytest.raises(UndefinedField) as exc_info:
        raise UndefinedField()
    assert str(exc_info.value) == 'Undefined field. Filed cannot be None.'
