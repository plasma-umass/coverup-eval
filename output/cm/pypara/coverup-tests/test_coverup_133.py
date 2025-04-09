# file pypara/monetary.py:638-639
# lines [638, 639]
# branches []

import pytest
from pypara.monetary import NoneMoney

def test_none_money_as_float_raises_type_error():
    none_money = NoneMoney()
    with pytest.raises(TypeError) as exc_info:
        none_money.as_float()
    assert str(exc_info.value) == "Undefined monetary values do not have quantity information."
