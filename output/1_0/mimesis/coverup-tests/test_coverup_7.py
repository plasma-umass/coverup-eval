# file mimesis/exceptions.py:27-31
# lines [27, 28, 30, 31]
# branches []

import pytest
from mimesis.exceptions import UndefinedSchema

def test_undefined_schema_exception():
    with pytest.raises(UndefinedSchema) as exc_info:
        raise UndefinedSchema()
    assert str(exc_info.value) == 'Schema should be defined in lambda.'
