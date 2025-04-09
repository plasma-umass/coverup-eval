# file: lib/ansible/plugins/lookup/ini.py:124-134
# asked: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}
# gained: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}

import pytest
import re
from ansible.module_utils.six.moves import configparser
from ansible.plugins.lookup.ini import LookupModule

@pytest.fixture
def mock_configparser(mocker):
    mock_cp = mocker.Mock()
    mocker.patch('ansible.plugins.lookup.ini.configparser.ConfigParser', return_value=mock_cp)
    return mock_cp

def test_get_value_single_value(mock_configparser):
    lookup = LookupModule()
    lookup.cp = mock_configparser
    mock_configparser.get.return_value = 'value'
    
    result = lookup.get_value('key', 'section', 'default', False)
    
    mock_configparser.get.assert_called_once_with('section', 'key')
    assert result == 'value'

def test_get_value_default(mock_configparser):
    lookup = LookupModule()
    lookup.cp = mock_configparser
    mock_configparser.get.side_effect = configparser.NoOptionError('key', 'section')
    
    result = lookup.get_value('key', 'section', 'default', False)
    
    mock_configparser.get.assert_called_once_with('section', 'key')
    assert result == 'default'

def test_get_value_regexp(mock_configparser):
    lookup = LookupModule()
    lookup.cp = mock_configparser
    mock_configparser.items.return_value = [('key1', 'value1'), ('key2', 'value2')]
    
    result = lookup.get_value('key.*', 'section', 'default', True)
    
    mock_configparser.items.assert_called_once_with('section')
    assert result == ['value1', 'value2']
