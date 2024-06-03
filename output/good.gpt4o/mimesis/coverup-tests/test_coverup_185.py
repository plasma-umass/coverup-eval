# file mimesis/builtins/pt_br.py:23-58
# lines [44]
# branches ['43->44']

import pytest
from mimesis.builtins.pt_br import BrazilSpecProvider

@pytest.fixture
def brazil_spec_provider():
    return BrazilSpecProvider()

def test_cpf_with_specific_digits(mocker, brazil_spec_provider):
    # Mock the random.randint method to control the output
    mocker.patch.object(brazil_spec_provider.random, 'randint', side_effect=[0, 0, 0, 0, 0, 0, 0, 0, 0])

    cpf = brazil_spec_provider.cpf(with_mask=False)
    
    # Assert that the CPF is correctly formatted
    assert cpf == '00000000000'

    # Now test with mask
    mocker.patch.object(brazil_spec_provider.random, 'randint', side_effect=[0, 0, 0, 0, 0, 0, 0, 0, 0])
    cpf_with_mask = brazil_spec_provider.cpf(with_mask=True)
    
    # Assert that the CPF with mask is correctly formatted
    assert cpf_with_mask == '000.000.000-00'
