# file pypara/monetary.py:1336-1337
# lines [1336, 1337]
# branches []

import pytest
from pypara.monetary import NonePrice, Price

def test_none_price_as_integer():
    none_price = NonePrice()
    with pytest.raises(TypeError) as exc_info:
        none_price.as_integer()
    assert str(exc_info.value) == "Undefined monetary values do not have quantity information."
