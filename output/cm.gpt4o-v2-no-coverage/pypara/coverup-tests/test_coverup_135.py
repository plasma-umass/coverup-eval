# file: pypara/monetary.py:1333-1334
# asked: {"lines": [1333, 1334], "branches": []}
# gained: {"lines": [1333, 1334], "branches": []}

import pytest
from pypara.monetary import NonePrice

def test_none_price_as_float():
    none_price = NonePrice()
    with pytest.raises(TypeError, match="Undefined monetary values do not have quantity information."):
        none_price.as_float()
