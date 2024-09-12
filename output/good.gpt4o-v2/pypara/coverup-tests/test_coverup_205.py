# file: pypara/monetary.py:1038-1040
# asked: {"lines": [1040], "branches": []}
# gained: {"lines": [1040], "branches": []}

import pytest
from pypara.monetary import Price

def test_price_int_method():
    with pytest.raises(TypeError):
        price = Price()
        int(price)
