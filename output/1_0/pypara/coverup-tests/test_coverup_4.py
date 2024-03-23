# file pypara/commons/numbers.py:53-57
# lines [53, 57]
# branches []

import pytest
from decimal import Decimal
from pypara.commons.numbers import make_quantizer

def test_make_quantizer():
    # Test with precision 0
    quantizer = make_quantizer(0)
    assert quantizer == Decimal("0.0"), "Quantizer with precision 0 should be 0.0"

    # Test with precision 3
    quantizer = make_quantizer(3)
    assert quantizer == Decimal("0.000"), "Quantizer with precision 3 should be 0.000"

    # Test with precision 5
    quantizer = make_quantizer(5)
    assert quantizer == Decimal("0.00000"), "Quantizer with precision 5 should be 0.00000"

    # Clean up is not necessary as the function does not modify any external state
