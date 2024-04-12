# file mimesis/builtins/ru.py:152-167
# lines [152, 160, 161, 162, 164, 165, 167]
# branches ['161->162', '161->164']

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

@pytest.fixture
def russia_provider():
    return RussiaSpecProvider()

def test_ogrn(russia_provider):
    ogrn = russia_provider.ogrn()
    assert len(ogrn) == 13
    assert ogrn.isdigit()
    assert int(ogrn[:-1]) % 11 % 10 == int(ogrn[-1])
