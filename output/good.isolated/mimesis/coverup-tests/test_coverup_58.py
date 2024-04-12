# file mimesis/providers/internet.py:32-41
# lines [32, 38, 39, 40, 41]
# branches []

import pytest
from mimesis.providers import BaseProvider
from mimesis.providers import File

class Internet(BaseProvider):
    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.__file = File(seed=self.seed)
        self._MAX_IPV4 = (2 ** 32) - 1
        self._MAX_IPV6 = (2 ** 128) - 1

# Test function
def test_internet_provider_initialization(mocker):
    # Mock the File class to ensure it is called with the correct seed
    mock_file_init = mocker.patch('mimesis.providers.File.__init__', return_value=None)
    seed = 12345
    internet_provider = Internet(seed=seed)
    
    # Assert that the File class was instantiated with the correct seed
    mock_file_init.assert_called_once_with(seed=seed)
    
    # Assert that the _MAX_IPV4 and _MAX_IPV6 attributes are set correctly
    assert internet_provider._MAX_IPV4 == (2 ** 32) - 1
    assert internet_provider._MAX_IPV6 == (2 ** 128) - 1
