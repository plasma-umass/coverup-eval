# file: lib/ansible/config/manager.py:187-195
# asked: {"lines": [187, 189, 190, 191, 192, 193, 194, 195], "branches": [[190, 191], [190, 195]]}
# gained: {"lines": [187, 189, 190, 191, 192, 193, 194, 195], "branches": [[190, 191], [190, 195]]}

import pytest
from configparser import ConfigParser
from ansible.config.manager import get_ini_config_value

def test_get_ini_config_value_with_valid_entry():
    config = ConfigParser()
    config.add_section('defaults')
    config.set('defaults', 'key', 'value')
    
    entry = {'section': 'defaults', 'key': 'key'}
    result = get_ini_config_value(config, entry)
    
    assert result == 'value'

def test_get_ini_config_value_with_invalid_entry():
    config = ConfigParser()
    config.add_section('defaults')
    
    entry = {'section': 'defaults', 'key': 'nonexistent_key'}
    result = get_ini_config_value(config, entry)
    
    assert result is None

def test_get_ini_config_value_with_no_section():
    config = ConfigParser()
    
    entry = {'section': 'nonexistent_section', 'key': 'key'}
    result = get_ini_config_value(config, entry)
    
    assert result is None

def test_get_ini_config_value_with_none_parser():
    entry = {'section': 'defaults', 'key': 'key'}
    result = get_ini_config_value(None, entry)
    
    assert result is None
