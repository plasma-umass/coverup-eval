# file: lib/ansible/plugins/lookup/ini.py:124-134
# asked: {"lines": [124, 126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}
# gained: {"lines": [124, 126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}

import pytest
import re
from ansible.module_utils.six.moves import configparser
from ansible.plugins.lookup.ini import LookupModule

@pytest.fixture
def lookup_module():
    class MockConfigParser:
        def __init__(self, data):
            self.data = data

        def items(self, section):
            return self.data.get(section, {}).items()

        def get(self, section, key):
            if section in self.data and key in self.data[section]:
                return self.data[section][key]
            raise configparser.NoOptionError(key, section)

    class MockLookupModule(LookupModule):
        def __init__(self, data):
            self.cp = MockConfigParser(data)

    return MockLookupModule

def test_get_value_with_regexp(lookup_module):
    data = {
        'section1': {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3'
        }
    }
    module = lookup_module(data)
    result = module.get_value('key[12]', 'section1', 'default', True)
    assert result == ['value1', 'value2']

def test_get_value_without_regexp_key_exists(lookup_module):
    data = {
        'section1': {
            'key1': 'value1'
        }
    }
    module = lookup_module(data)
    result = module.get_value('key1', 'section1', 'default', False)
    assert result == 'value1'

def test_get_value_without_regexp_key_not_exists(lookup_module):
    data = {
        'section1': {}
    }
    module = lookup_module(data)
    result = module.get_value('key1', 'section1', 'default', False)
    assert result == 'default'
