# file: pypara/monetary.py:1336-1337
# asked: {"lines": [1336, 1337], "branches": []}
# gained: {"lines": [1336, 1337], "branches": []}

import pytest
from pypara.monetary import NonePrice

def test_none_price_as_integer():
    none_price = NonePrice()
    with pytest.raises(TypeError, match="Undefined monetary values do not have quantity information."):
        none_price.as_integer()
