# file mimesis/builtins/ru.py:125-150
# lines [125, 130, 131, 132, 133, 135, 136, 138, 139, 140, 142, 143, 144, 146, 147, 148, 149, 150]
# branches ['138->139', '138->140', '143->144', '143->146']

import pytest
from mimesis.builtins.ru import RussiaSpecProvider
from mimesis.random import Random

@pytest.fixture
def russia_spec_provider(mocker):
    mocker.patch.object(Random, 'randint', side_effect=[1] + [0] * 9)
    return RussiaSpecProvider()

def test_inn_full_coverage(russia_spec_provider):
    inn = russia_spec_provider.inn()
    assert len(inn) == 12
    assert inn.isdigit()
    assert inn.startswith('1')
