# file: pypara/commons/numbers.py:53-57
# asked: {"lines": [53, 57], "branches": []}
# gained: {"lines": [53, 57], "branches": []}

import pytest
from decimal import Decimal
from pypara.commons.numbers import make_quantizer

def test_make_quantizer():
    # Test with precision 0
    quantizer = make_quantizer(0)
    assert quantizer == Decimal("0.")

    # Test with precision 1
    quantizer = make_quantizer(1)
    assert quantizer == Decimal("0.0")

    # Test with precision 5
    quantizer = make_quantizer(5)
    assert quantizer == Decimal("0.00000")

    # Test with precision 10
    quantizer = make_quantizer(10)
    assert quantizer == Decimal("0.0000000000")
