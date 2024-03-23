# file pypara/commons/numbers.py:67-88
# lines [88]
# branches []

import pytest
from decimal import Decimal
from typing import Iterable, Optional
from pypara.commons.numbers import isum

class Amount(Decimal):
    pass

class Quantity(Decimal):
    pass

@pytest.fixture
def mock_decimal_cast(mocker):
    mocker.patch('pypara.commons.numbers.cast', return_value=Amount('0'))

def test_isum_with_cast_start_to_amount(mock_decimal_cast):
    # Test to cover line 88 with start=None and xs being an empty list
    result = isum([], start=None)
    assert result == Amount('0'), "The result should be an Amount with value 0"
