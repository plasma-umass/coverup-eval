# file: lib/ansible/config/manager.py:187-195
# asked: {"lines": [187, 189, 190, 191, 192, 193, 194, 195], "branches": [[190, 191], [190, 195]]}
# gained: {"lines": [187, 189, 190, 191, 192, 193, 194, 195], "branches": [[190, 191], [190, 195]]}

import pytest
from unittest.mock import Mock
from ansible.config.manager import get_ini_config_value

def test_get_ini_config_value_with_valid_entry():
    p = Mock()
    p.get.return_value = 'value'
    entry = {'section': 'section1', 'key': 'key1'}
    
    result = get_ini_config_value(p, entry)
    
    p.get.assert_called_once_with('section1', 'key1', raw=True)
    assert result == 'value'

def test_get_ini_config_value_with_default_section_and_key():
    p = Mock()
    p.get.return_value = 'default_value'
    entry = {}
    
    result = get_ini_config_value(p, entry)
    
    p.get.assert_called_once_with('defaults', '', raw=True)
    assert result == 'default_value'

def test_get_ini_config_value_with_exception():
    p = Mock()
    p.get.side_effect = Exception("Test Exception")
    entry = {'section': 'section1', 'key': 'key1'}
    
    result = get_ini_config_value(p, entry)
    
    p.get.assert_called_once_with('section1', 'key1', raw=True)
    assert result is None

def test_get_ini_config_value_with_none_p():
    p = None
    entry = {'section': 'section1', 'key': 'key1'}
    
    result = get_ini_config_value(p, entry)
    
    assert result is None
