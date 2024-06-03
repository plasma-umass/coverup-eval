# file mimesis/builtins/pt_br.py:14-16
# lines [14, 16]
# branches []

import pytest
from mimesis.builtins.pt_br import BrazilSpecProvider

def test_brazil_spec_provider_initialization():
    # Test initialization without seed
    provider = BrazilSpecProvider()
    assert isinstance(provider, BrazilSpecProvider)
    assert provider.locale == 'pt-br'
    
    # Test initialization with seed
    seed = 12345
    provider_with_seed = BrazilSpecProvider(seed=seed)
    assert isinstance(provider_with_seed, BrazilSpecProvider)
    assert provider_with_seed.locale == 'pt-br'
    assert provider_with_seed.seed == seed
