# file: lib/ansible/config/manager.py:187-195
# asked: {"lines": [187, 189, 190, 191, 192, 193, 194, 195], "branches": [[190, 191], [190, 195]]}
# gained: {"lines": [187, 189, 190, 191, 192, 193, 194, 195], "branches": [[190, 191], [190, 195]]}

import pytest
from unittest.mock import Mock

from ansible.config.manager import get_ini_config_value

def test_get_ini_config_value_with_valid_entry():
    mock_parser = Mock()
    mock_parser.get.return_value = 'test_value'
    entry = {'section': 'test_section', 'key': 'test_key'}
    
    result = get_ini_config_value(mock_parser, entry)
    
    assert result == 'test_value'
    mock_parser.get.assert_called_once_with('test_section', 'test_key', raw=True)

def test_get_ini_config_value_with_exception():
    mock_parser = Mock()
    mock_parser.get.side_effect = Exception("Test Exception")
    entry = {'section': 'test_section', 'key': 'test_key'}
    
    result = get_ini_config_value(mock_parser, entry)
    
    assert result is None
    mock_parser.get.assert_called_once_with('test_section', 'test_key', raw=True)

def test_get_ini_config_value_with_none_parser():
    entry = {'section': 'test_section', 'key': 'test_key'}
    
    result = get_ini_config_value(None, entry)
    
    assert result is None
