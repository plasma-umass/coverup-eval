# file mimesis/providers/base.py:20-22
# lines [20, 21]
# branches []

import pytest
from mimesis.providers.base import BaseProvider

def test_base_provider_initialization():
    # Test the initialization of BaseProvider
    provider = BaseProvider()
    assert isinstance(provider, BaseProvider)

@pytest.fixture
def mock_base_provider(mocker):
    # Mock the BaseProvider class
    mocker.patch('mimesis.providers.base.BaseProvider', autospec=True)
    return BaseProvider()

def test_mocked_base_provider(mock_base_provider):
    # Test the mocked BaseProvider
    assert isinstance(mock_base_provider, BaseProvider)
