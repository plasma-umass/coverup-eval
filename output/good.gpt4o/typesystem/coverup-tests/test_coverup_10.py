# file typesystem/fields.py:206-236
# lines [206, 209, 210, 211, 212, 213, 214, 217, 219, 220, 221, 222, 224, 225, 227, 228, 231, 232, 233, 234, 235, 236]
# branches []

import pytest
import decimal
from typesystem.fields import Field

class TestNumberField:
    def test_number_field_initialization(self):
        from typesystem.fields import Number

        # Test with all parameters
        number = Number(
            minimum=1,
            maximum=10,
            exclusive_minimum=0,
            exclusive_maximum=11,
            precision="0.01",
            multiple_of=2
        )
        assert number.minimum == 1
        assert number.maximum == 10
        assert number.exclusive_minimum == 0
        assert number.exclusive_maximum == 11
        assert number.precision == "0.01"
        assert number.multiple_of == 2

        # Test with decimal.Decimal values
        number = Number(
            minimum=decimal.Decimal('1.1'),
            maximum=decimal.Decimal('10.1'),
            exclusive_minimum=decimal.Decimal('0.1'),
            exclusive_maximum=decimal.Decimal('11.1'),
            multiple_of=decimal.Decimal('2.1')
        )
        assert number.minimum == decimal.Decimal('1.1')
        assert number.maximum == decimal.Decimal('10.1')
        assert number.exclusive_minimum == decimal.Decimal('0.1')
        assert number.exclusive_maximum == decimal.Decimal('11.1')
        assert number.multiple_of == decimal.Decimal('2.1')

        # Test with float values
        number = Number(
            minimum=1.1,
            maximum=10.1,
            exclusive_minimum=0.1,
            exclusive_maximum=11.1,
            multiple_of=2.1
        )
        assert number.minimum == 1.1
        assert number.maximum == 10.1
        assert number.exclusive_minimum == 0.1
        assert number.exclusive_maximum == 11.1
        assert number.multiple_of == 2.1

        # Test with None values
        number = Number()
        assert number.minimum is None
        assert number.maximum is None
        assert number.exclusive_minimum is None
        assert number.exclusive_maximum is None
        assert number.precision is None
        assert number.multiple_of is None

    def test_number_field_invalid_initialization(self):
        from typesystem.fields import Number

        with pytest.raises(AssertionError):
            Number(minimum="invalid")

        with pytest.raises(AssertionError):
            Number(maximum="invalid")

        with pytest.raises(AssertionError):
            Number(exclusive_minimum="invalid")

        with pytest.raises(AssertionError):
            Number(exclusive_maximum="invalid")

        with pytest.raises(AssertionError):
            Number(multiple_of="invalid")
