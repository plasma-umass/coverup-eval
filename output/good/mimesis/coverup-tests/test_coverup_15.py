# file mimesis/builtins/ru.py:169-182
# lines [169, 177, 178, 179, 180, 181, 182]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider
from mimesis import Generic

@pytest.fixture
def russia_provider():
    return RussiaSpecProvider(Generic().random)

def test_bic(russia_provider):
    bic = russia_provider.bic()
    assert bic.startswith('04')
    assert len(bic) == 9
    assert 50 <= int(bic[6:]) <= 999
