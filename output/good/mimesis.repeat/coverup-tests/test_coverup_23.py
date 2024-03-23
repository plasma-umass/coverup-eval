# file mimesis/builtins/ru.py:169-182
# lines [169, 177, 178, 179, 180, 181, 182]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider
from mimesis.random import Random

@pytest.fixture
def russia_provider(mocker):
    mocker.patch('mimesis.random.Random', return_value=Random())
    return RussiaSpecProvider()

def test_bic(russia_provider):
    bic = russia_provider.bic()
    assert len(bic) == 9
    assert bic[:2] == '04'
    assert 1 <= int(bic[2:4]) <= 10
    assert 0 <= int(bic[4:6]) <= 99
    assert 50 <= int(bic[6:]) <= 999
