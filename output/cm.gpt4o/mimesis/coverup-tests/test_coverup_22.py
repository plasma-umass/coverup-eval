# file mimesis/builtins/ru.py:169-182
# lines [169, 177, 178, 179, 180, 181, 182]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

@pytest.fixture
def russia_spec_provider():
    return RussiaSpecProvider()

def test_bic(russia_spec_provider):
    bic = russia_spec_provider.bic()
    assert len(bic) == 9
    assert bic.startswith('04')
    assert bic[2:4].isdigit()
    assert bic[4:6].isdigit()
    assert bic[6:9].isdigit()
    assert 1 <= int(bic[2:4]) <= 10
    assert 0 <= int(bic[4:6]) <= 99
    assert 50 <= int(bic[6:9]) <= 999
