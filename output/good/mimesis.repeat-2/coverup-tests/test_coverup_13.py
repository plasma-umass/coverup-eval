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
    with pytest.raises(ValueError) as excinfo:
        rnd.randints(amount=0)
    assert "Amount out of range." in str(excinfo.value)

# Ensure that the test does not affect other tests by cleaning up
def test_cleanup(mocker):
    mocker.patch.object(Random, 'randints', return_value=[1, 2, 3])
    rnd = Random()
    assert rnd.randints() == [1, 2, 3]
    mocker.stopall()
    # After stopping all mocks, the original method should work as expected
    result = rnd.randints()
    assert len(result) == 3
    assert all(1 <= num < 100 for num in result)
