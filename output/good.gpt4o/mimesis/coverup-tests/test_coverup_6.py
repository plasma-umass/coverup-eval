# file mimesis/random.py:32-46
# lines [32, 33, 42, 43, 45, 46]
# branches ['42->43', '42->45']

import pytest
from mimesis.random import Random

def test_randints():
    random_instance = Random()

    # Test normal case
    result = random_instance.randints(amount=5, a=10, b=20)
    assert len(result) == 5
    assert all(10 <= x < 20 for x in result)

    # Test edge case where amount is 1
    result = random_instance.randints(amount=1, a=0, b=1)
    assert len(result) == 1
    assert 0 <= result[0] < 1

    # Test edge case where amount is 0 (should raise ValueError)
    with pytest.raises(ValueError):
        random_instance.randints(amount=0, a=10, b=20)

    # Test edge case where amount is negative (should raise ValueError)
    with pytest.raises(ValueError):
        random_instance.randints(amount=-1, a=10, b=20)
