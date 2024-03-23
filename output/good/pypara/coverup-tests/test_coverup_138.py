# file pypara/monetary.py:641-642
# lines [641, 642]
# branches []

import pytest
from pypara.monetary import NoneMoney

def test_none_money_as_integer_raises_type_error():
    none_money = NoneMoney()
    with pytest.raises(TypeError) as exc_info:
        none_money.as_integer()
    assert str(exc_info.value) == "Undefined monetary values do not have quantity information."
