# file mimesis/builtins/pt_br.py:23-58
# lines [23, 32, 39, 40, 41, 42, 43, 44, 45, 47, 48, 50, 51, 52, 54, 56, 57, 58]
# branches ['40->41', '40->42', '43->44', '43->45', '56->57', '56->58']

import pytest
from mimesis.builtins.pt_br import BrazilSpecProvider

@pytest.fixture
def brazil_spec_provider():
    return BrazilSpecProvider()

def test_cpf_with_mask(brazil_spec_provider):
    cpf = brazil_spec_provider.cpf(with_mask=True)
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    assert cpf.replace('.', '').replace('-', '').isdigit()

def test_cpf_without_mask(brazil_spec_provider):
    cpf = brazil_spec_provider.cpf(with_mask=False)
    assert len(cpf) == 11
    assert cpf.isdigit()
