# file typesystem/fields.py:687-689
# lines [687, 688, 689]
# branches []

import pytest
from typesystem.fields import Time
from typesystem import ValidationError
from datetime import time

def test_time_field():
    # Test valid time
    time_field = Time()
    valid_time = "12:34:56"
    expected_time = time(12, 34, 56)
    assert time_field.validate(valid_time) == expected_time

    # Test invalid time
    with pytest.raises(ValidationError):
        invalid_time = "25:61:61"
        time_field.validate(invalid_time)
