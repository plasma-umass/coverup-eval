# file pypara/monetary.py:1333-1334
# lines [1333, 1334]
# branches []

import pytest
from pypara.monetary import NonePrice

def test_none_price_as_float():
    none_price = NonePrice()
    with pytest.raises(TypeError) as exc_info:
        none_price.as_float()
    assert str(exc_info.value) == "Undefined monetary values do not have quantity information."
