# file pypara/monetary.py:1369-1370
# lines [1369, 1370]
# branches []

import pytest
from pypara.monetary import Price, NonePrice

def test_none_price_floor_divide():
    none_price = NonePrice()
    other_value = 10  # This can be any numeric value

    result = none_price.floor_divide(other_value)

    assert result is none_price, "The result should be the same NonePrice instance"

# Ensure to clean up if there are any side effects (though in this case, there shouldn't be any)
