# file: pypara/monetary.py:638-639
# asked: {"lines": [638, 639], "branches": []}
# gained: {"lines": [638, 639], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

def test_none_money_as_float_raises_type_error():
    none_money = NoneMoney()
    with pytest.raises(TypeError, match="Undefined monetary values do not have quantity information."):
        none_money.as_float()
