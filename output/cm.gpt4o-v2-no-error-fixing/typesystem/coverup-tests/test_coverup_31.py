# file: typesystem/fields.py:687-689
# asked: {"lines": [687, 688, 689], "branches": []}
# gained: {"lines": [687, 688, 689], "branches": []}

import pytest
from typesystem.fields import Time

def test_time_init():
    # Create an instance of Time with no additional arguments
    time_field = Time()
    
    # Assert that the format is set to "time"
    assert time_field.format == "time"
    
    # Create an instance of Time with additional arguments
    time_field_with_args = Time(allow_blank=True, max_length=5)
    
    # Assert that the format is still set to "time"
    assert time_field_with_args.format == "time"
    
    # Assert that other arguments are set correctly
    assert time_field_with_args.allow_blank is True
    assert time_field_with_args.max_length == 5
