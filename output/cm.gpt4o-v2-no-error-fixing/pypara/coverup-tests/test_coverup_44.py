# file: pypara/monetary.py:641-642
# asked: {"lines": [641, 642], "branches": []}
# gained: {"lines": [641, 642], "branches": []}

import pytest
from pypara.monetary import NoneMoney

def test_none_money_as_integer_raises_type_error():
    none_money = NoneMoney()
    with pytest.raises(TypeError, match="Undefined monetary values do not have quantity information."):
        none_money.as_integer()
