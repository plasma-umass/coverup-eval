# file mimesis/builtins/pl.py:16-18
# lines [16, 18]
# branches []

import pytest
from mimesis.builtins.pl import PolandSpecProvider
from mimesis.providers.base import BaseProvider

def test_poland_spec_provider_initialization():
    # Test initialization without seed
    provider = PolandSpecProvider()
    assert isinstance(provider, PolandSpecProvider)
    assert provider.locale == 'pl'

    # Test initialization with seed
    seed = 12345
    provider_with_seed = PolandSpecProvider(seed=seed)
    assert isinstance(provider_with_seed, PolandSpecProvider)
    assert provider_with_seed.locale == 'pl'
    assert provider_with_seed.seed == seed
