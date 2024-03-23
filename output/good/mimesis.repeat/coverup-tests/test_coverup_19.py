# file mimesis/random.py:32-46
# lines [32, 33, 42, 43, 45, 46]
# branches ['42->43', '42->45']

import pytest
from mimesis.random import Random

def test_randints():
    random_instance = Random()

    # Test for default parameters
    default_ints = random_instance.randints()
    assert len(default_ints) == 3
    assert all(1 <= num <= 100 for num in default_ints)

    # Test for custom parameters
    custom_ints = random_instance.randints(amount=5, a=10, b=50)
    assert len(custom_ints) == 5
    assert all(10 <= num <= 50 for num in custom_ints)

    # Test for amount equal to zero should raise ValueError
    with pytest.raises(ValueError):
        random_instance.randints(amount=0)

    # Test for amount less than zero should raise ValueError
    with pytest.raises(ValueError):
        random_instance.randints(amount=-1)

# Clean up is not necessary as each test function will create a new instance of Random
# and no state is shared between tests.
