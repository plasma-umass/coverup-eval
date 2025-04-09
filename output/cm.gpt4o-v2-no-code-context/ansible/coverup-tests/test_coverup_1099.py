# file: lib/ansible/config/manager.py:187-195
# asked: {"lines": [], "branches": [[190, 195]]}
# gained: {"lines": [], "branches": [[190, 195]]}

import pytest
from unittest.mock import Mock

# Assuming the function is a standalone function in ansible/config/manager.py
from ansible.config.manager import get_ini_config_value

@pytest.fixture
def mock_parser():
    return Mock()

def test_get_ini_config_value_with_valid_parser(mock_parser):
    mock_parser.get.return_value = 'test_value'
    entry = {'section': 'defaults', 'key': 'test_key'}
    
    result = get_ini_config_value(mock_parser, entry)
    
    mock_parser.get.assert_called_once_with('defaults', 'test_key', raw=True)
    assert result == 'test_value'

def test_get_ini_config_value_with_exception(mock_parser):
    mock_parser.get.side_effect = Exception("Test Exception")
    entry = {'section': 'defaults', 'key': 'test_key'}
    
    result = get_ini_config_value(mock_parser, entry)
    
    mock_parser.get.assert_called_once_with('defaults', 'test_key', raw=True)
    assert result is None

def test_get_ini_config_value_with_none_parser():
    entry = {'section': 'defaults', 'key': 'test_key'}
    
    result = get_ini_config_value(None, entry)
    
    assert result is None
