# file mimesis/builtins/ru.py:169-182
# lines [169, 177, 178, 179, 180, 181, 182]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider
from mimesis.random import Random

@pytest.fixture
def russia_spec_provider(mocker):
    mocker.patch.object(Random, 'randint', side_effect=[1, 0, 50])
    return RussiaSpecProvider()

def test_bic(russia_spec_provider):
    bic = russia_spec_provider.bic()
    assert bic.startswith('04')
    assert len(bic) == 9
    # Since we mocked randint to return 1, 0, 50 in that order, we expect the BIC to be:
    assert bic == '040100050'
