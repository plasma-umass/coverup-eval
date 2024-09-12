# file: typesystem/fields.py:687-689
# asked: {"lines": [687, 688, 689], "branches": []}
# gained: {"lines": [687, 688, 689], "branches": []}

import pytest
from typesystem.fields import Time

def test_time_field_initialization():
    # Create an instance of Time with additional keyword arguments
    time_field = Time(title="Test Time Field", description="A test time field")

    # Assert that the instance is created and has the correct attributes
    assert time_field.format == "time"
    assert time_field.title == "Test Time Field"
    assert time_field.description == "A test time field"
