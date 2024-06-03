# file pypara/monetary.py:1022-1024
# lines [1024]
# branches []

import pytest
from abc import ABC, abstractmethod

# Assuming the Price class is defined in pypara.monetary
from pypara.monetary import Price

def test_price_bool_abstract_method():
    with pytest.raises(TypeError):
        class TestPrice(Price):
            pass

        test_price_instance = TestPrice()
        bool(test_price_instance)
