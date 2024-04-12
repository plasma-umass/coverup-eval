# file mimesis/builtins/ru.py:66-75
# lines [66, 74, 75]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

def test_passport_number():
    provider = RussiaSpecProvider()
    passport_number = provider.passport_number()
    assert 100000 <= passport_number <= 999999
