# file mimesis/providers/numbers.py:17-20
# lines [17, 18, 20]
# branches []

import pytest
from mimesis.providers.numbers import Numbers

def test_numbers_meta():
    numbers = Numbers()
    assert numbers.Meta.name == 'numbers'
