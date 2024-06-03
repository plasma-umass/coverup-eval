# file mimesis/builtins/en.py:16-18
# lines [16, 18]
# branches []

import pytest
from mimesis.builtins.en import USASpecProvider

def test_usa_spec_provider_initialization():
    # Test initialization without seed
    provider = USASpecProvider()
    assert isinstance(provider, USASpecProvider)
    assert provider.locale == 'en'
    
    # Test initialization with seed
    seed = 12345
    provider_with_seed = USASpecProvider(seed=seed)
    assert isinstance(provider_with_seed, USASpecProvider)
    assert provider_with_seed.locale == 'en'
    assert provider_with_seed.seed == seed
