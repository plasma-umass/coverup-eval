# file: lib/ansible/plugins/lookup/ini.py:124-134
# asked: {"lines": [124, 126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}
# gained: {"lines": [124, 126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.lookup.ini import LookupModule
from ansible.module_utils.six.moves import configparser

@pytest.fixture
def lookup_module():
    lm = LookupModule()
    lm.cp = MagicMock()
    return lm

def test_get_value_with_regexp(lookup_module):
    lookup_module.cp.items.return_value = [('key1', 'value1'), ('key2', 'value2')]
    result = lookup_module.get_value('key.*', 'section', 'default', True)
    assert result == ['value1', 'value2']

def test_get_value_without_regexp_key_exists(lookup_module):
    lookup_module.cp.get.return_value = 'value1'
    result = lookup_module.get_value('key1', 'section', 'default', False)
    assert result == 'value1'

def test_get_value_without_regexp_key_not_exists(lookup_module):
    lookup_module.cp.get.side_effect = configparser.NoOptionError('key1', 'section')
    result = lookup_module.get_value('key1', 'section', 'default', False)
    assert result == 'default'
