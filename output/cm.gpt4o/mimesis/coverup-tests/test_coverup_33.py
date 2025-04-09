# file mimesis/providers/base.py:23-33
# lines [23, 29, 30, 32, 33]
# branches ['32->exit', '32->33']

import pytest
from mimesis.providers.base import BaseProvider

def test_base_provider_with_seed(mocker):
    # Mock the reseed method to ensure it gets called
    mock_reseed = mocker.patch.object(BaseProvider, 'reseed', autospec=True)
    
    seed = 12345
    provider = BaseProvider(seed=seed)
    
    # Assert that the seed is set correctly
    assert provider.seed == seed
    
    # Assert that reseed was called with the correct seed
    mock_reseed.assert_called_once_with(provider, seed)

def test_base_provider_without_seed(mocker):
    # Mock the reseed method to ensure it does not get called
    mock_reseed = mocker.patch.object(BaseProvider, 'reseed', autospec=True)
    
    provider = BaseProvider(seed=None)
    
    # Assert that the seed is None
    assert provider.seed is None
    
    # Assert that reseed was not called
    mock_reseed.assert_not_called()
