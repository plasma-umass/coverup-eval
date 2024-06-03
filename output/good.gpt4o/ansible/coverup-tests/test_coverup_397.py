# file lib/ansible/plugins/lookup/ini.py:124-134
# lines [124, 126, 127, 128, 130, 131, 132, 133, 134]
# branches ['126->127', '126->128']

import pytest
import configparser
import re
from ansible.plugins.lookup.ini import LookupModule

@pytest.fixture
def mock_configparser(mocker):
    mock_cp = mocker.Mock()
    mocker.patch('ansible.plugins.lookup.ini.configparser.ConfigParser', return_value=mock_cp)
    return mock_cp

def test_get_value_with_regexp(mock_configparser):
    lookup = LookupModule()
    lookup.cp = mock_configparser
    mock_configparser.items.return_value = [('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]
    
    result = lookup.get_value('key[12]', 'section', 'default', True)
    
    assert result == ['value1', 'value2']

def test_get_value_no_option_error(mock_configparser):
    lookup = LookupModule()
    lookup.cp = mock_configparser
    mock_configparser.get.side_effect = configparser.NoOptionError('key', 'section')
    
    result = lookup.get_value('key', 'section', 'default', False)
    
    assert result == 'default'

def test_get_value_single_value(mock_configparser):
    lookup = LookupModule()
    lookup.cp = mock_configparser
    mock_configparser.get.return_value = 'value'
    
    result = lookup.get_value('key', 'section', 'default', False)
    
    assert result == 'value'
