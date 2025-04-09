# file mimesis/providers/internet.py:32-41
# lines [32, 38, 39, 40, 41]
# branches []

import pytest
from mimesis.providers.internet import Internet
from mimesis.providers.file import File

@pytest.fixture
def internet_provider():
    return Internet()

def test_internet_provider_initialization(mocker, internet_provider):
    # Mock the File class to ensure it does not affect other tests
    mock_file = mocker.patch('mimesis.providers.internet.File', autospec=True)
    mock_file_instance = mock_file.return_value
    mock_file_instance.seed = internet_provider.seed
    
    # Create an instance of Internet provider
    provider = Internet()
    
    # Assertions to verify the initialization
    assert provider._MAX_IPV4 == (2 ** 32) - 1
    assert provider._MAX_IPV6 == (2 ** 128) - 1
    assert isinstance(provider._Internet__file, File)
    assert provider._Internet__file.seed == provider.seed
