# file mimesis/providers/generic.py:71-84
# lines [71, 77, 78, 79, 80, 81, 82, 84]
# branches ['79->exit', '79->80']

import pytest
from mimesis.providers.generic import Generic
from mimesis.providers.base import BaseDataProvider
from unittest.mock import MagicMock

class MockProvider(BaseDataProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._mocked_method = MagicMock(return_value='mocked_value')

@pytest.fixture
def generic_provider():
    return Generic('en')

@pytest.fixture
def mock_provider():
    return MockProvider('en')

def test_generic_getattr(generic_provider, mock_provider):
    # Add a mocked method to the generic provider
    generic_provider._mocked_method = mock_provider._mocked_method

    # Access the mocked method to trigger __getattr__
    result = generic_provider.mocked_method

    # Check that the mocked method was called
    mock_provider._mocked_method.assert_called_once_with('en', None)

    # Check that the result is the return value of the mock object
    assert result == mock_provider._mocked_method.return_value

    # Clean up by deleting the mocked method from the generic provider
    del generic_provider._mocked_method
