# file mimesis/providers/person.py:328-339
# lines [328, 338, 339]
# branches []

import pytest
from mimesis.providers.person import Person

@pytest.fixture
def person():
    return Person()

def test_height(person):
    # Test the default range
    default_height = person.height()
    assert 1.5 <= float(default_height) <= 2.0

    # Test a custom range
    custom_min, custom_max = 1.6, 1.8
    custom_height = person.height(minimum=custom_min, maximum=custom_max)
    assert custom_min <= float(custom_height) <= custom_max

    # Test the edge cases
    min_height = person.height(minimum=1.5, maximum=1.5)
    assert float(min_height) == 1.5

    max_height = person.height(minimum=2.0, maximum=2.0)
    assert float(max_height) == 2.0

    # The original mimesis code does not raise a ValueError for reversed min and max,
    # so we remove the incorrect test case.
