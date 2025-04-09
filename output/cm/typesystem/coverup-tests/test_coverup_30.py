# file typesystem/fields.py:309-313
# lines [309, 310, 312, 313]
# branches []

import decimal
import pytest
from typesystem.fields import Decimal

@pytest.fixture
def cleanup_decimal():
    # Setup: None required for this test
    yield
    # Teardown: None required for this test

def test_decimal_serialize(cleanup_decimal):
    decimal_field = Decimal()

    # Test serialization of None
    assert decimal_field.serialize(None) is None

    # Test serialization of a decimal.Decimal object
    value = decimal.Decimal('10.5')
    serialized_value = decimal_field.serialize(value)
    assert serialized_value == 10.5
    assert isinstance(serialized_value, float)

    # Test serialization of a float
    value = 10.5
    serialized_value = decimal_field.serialize(value)
    assert serialized_value == 10.5
    assert isinstance(serialized_value, float)
