# file semantic_release/settings.py:121-135
# lines [121, 126, 127, 128, 129, 130, 131, 132, 133, 135]
# branches ['128->129', '128->133', '129->130', '129->133', '131->129', '131->132']

import pytest
from unittest.mock import patch
from semantic_release.settings import overload_configuration

@pytest.fixture
def mock_config():
    with patch('semantic_release.settings.config') as mock_config:
        yield mock_config

def test_overload_configuration_with_define(mock_config):
    @overload_configuration
    def dummy_function(*args, **kwargs):
        pass

    test_args = (1, 2)
    test_kwargs = {'define': ['key1=value1', 'key2=value2']}
    dummy_function(*test_args, **test_kwargs)

    assert mock_config.__setitem__.call_count == 2
    mock_config.__setitem__.assert_any_call('key1', 'value1')
    mock_config.__setitem__.assert_any_call('key2', 'value2')

def test_overload_configuration_without_define(mock_config):
    @overload_configuration
    def dummy_function(*args, **kwargs):
        pass

    test_args = (1, 2)
    test_kwargs = {}
    dummy_function(*test_args, **test_kwargs)

    mock_config.__setitem__.assert_not_called()
