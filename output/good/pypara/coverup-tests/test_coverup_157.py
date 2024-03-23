# file pypara/monetary.py:680-681
# lines [680, 681]
# branches []

import pytest
from pypara.monetary import NoneMoney

def test_none_money_gt():
    none_money = NoneMoney()
    other_money = NoneMoney()  # Assuming NoneMoney can be compared to itself

    # Assert that NoneMoney is never greater than any other NoneMoney instance
    assert not none_money.gt(other_money)

    # Clean up is not necessary as no external state is modified
