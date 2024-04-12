# file mimesis/random.py:32-46
# lines [32, 33, 42, 43, 45, 46]
# branches ['42->43', '42->45']

import pytest
from mimesis.random import Random

def test_randints():
    rnd = Random()
    amount = 5
    a = 10
    b = 20
    result = rnd.randints(amount, a, b)
    assert len(result) == amount
    assert all(a <= num < b for num in result)

def test_randints_with_invalid_amount():
    rnd = Random()
    with pytest.raises(ValueError) as exc_info:
        rnd.randints(0)
    assert str(exc_info.value) == 'Amount out of range.'
