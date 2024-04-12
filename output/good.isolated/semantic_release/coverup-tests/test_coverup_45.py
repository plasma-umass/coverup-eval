# file semantic_release/settings.py:121-135
# lines []
# branches ['131->129']

import pytest
from unittest.mock import patch
from semantic_release.settings import overload_configuration

@pytest.fixture
def mock_config():
    with patch('semantic_release.settings.config', {}) as mock_config:
        yield mock_config

def test_overload_configuration_with_single_define(mock_config):
    @overload_configuration
    def dummy_function(*args, **kwargs):
        pass

    dummy_function(define=['name=value'])
    assert mock_config['name'] == 'value'

def test_overload_configuration_with_no_equals_sign(mock_config):
    @overload_configuration
    def dummy_function(*args, **kwargs):
        pass

    dummy_function(define=['name'])
    assert 'name' not in mock_config
