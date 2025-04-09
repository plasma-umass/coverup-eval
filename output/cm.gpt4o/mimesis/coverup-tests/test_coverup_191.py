# file mimesis/builtins/pt_br.py:60-101
# lines [85]
# branches ['79->81', '84->85']

import pytest
from mimesis.builtins.pt_br import BrazilSpecProvider

@pytest.fixture
def brazil_spec_provider():
    return BrazilSpecProvider()

def test_cnpj_with_mask(brazil_spec_provider, mocker):
    mocker.patch.object(brazil_spec_provider.random, 'randint', side_effect=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    cnpj = brazil_spec_provider.cnpj(with_mask=True)
    assert cnpj == '00.000.000/0000-00'

def test_cnpj_without_mask(brazil_spec_provider, mocker):
    mocker.patch.object(brazil_spec_provider.random, 'randint', side_effect=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    cnpj = brazil_spec_provider.cnpj(with_mask=False)
    assert cnpj == '00000000000000'
