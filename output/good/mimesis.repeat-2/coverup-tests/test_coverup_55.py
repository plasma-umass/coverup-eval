# file mimesis/builtins/ru.py:66-75
# lines [66, 74, 75]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

@pytest.fixture
def russia_spec_provider():
    return RussiaSpecProvider()

def test_passport_number(russia_spec_provider):
    passport_number = russia_spec_provider.passport_number()
    assert 100000 <= passport_number <= 999999
