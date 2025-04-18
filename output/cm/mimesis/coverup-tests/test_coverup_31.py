# file mimesis/builtins/ru.py:184-225
# lines [184, 192, 221, 222, 223, 224, 225]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider
from mimesis.random import Random

@pytest.fixture
def russia_spec_provider(mocker):
    mocker.patch.object(Random, 'randint', side_effect=lambda x, y: y)
    return RussiaSpecProvider()

def test_kpp(russia_spec_provider):
    kpp = russia_spec_provider.kpp()
    assert len(kpp) == 9
    assert kpp[:4] == '9998'
    assert kpp[4:6] == '99'
    assert kpp[6:] == '999'
