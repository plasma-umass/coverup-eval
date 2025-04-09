# file: pypara/monetary.py:1022-1024
# asked: {"lines": [1024], "branches": []}
# gained: {"lines": [1024], "branches": []}

import pytest
from pypara.monetary import Price

def test_price_bool():
    with pytest.raises(TypeError):
        price_instance = Price()
        bool(price_instance)
