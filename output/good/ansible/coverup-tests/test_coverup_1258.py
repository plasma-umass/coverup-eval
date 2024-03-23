# file lib/ansible/plugins/lookup/ini.py:124-134
# lines [124, 126, 127, 128, 130, 131, 132, 133, 134]
# branches ['126->127', '126->128']

import pytest
import configparser
from ansible.plugins.lookup.ini import LookupModule
from unittest.mock import MagicMock

@pytest.fixture
def ini_lookup():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    return lookup

def test_get_value_with_regexp(ini_lookup, tmp_path):
    # Setup the ini file
    ini_file = tmp_path / "test.ini"
    ini_file.write_text("[section1]\nkey1=value1\nkey2=value2\n")

    # Read the ini file with configparser
    ini_lookup.cp.read(str(ini_file))

    # Test get_value with regexp
    values = ini_lookup.get_value('key[12]', 'section1', 'default', is_regexp=True)
    assert 'value1' in values
    assert 'value2' in values

def test_get_value_without_regexp(ini_lookup, tmp_path):
    # Setup the ini file
    ini_file = tmp_path / "test.ini"
    ini_file.write_text("[section1]\nkey=value\n")

    # Read the ini file with configparser
    ini_lookup.cp.read(str(ini_file))

    # Test get_value without regexp
    value = ini_lookup.get_value('key', 'section1', 'default', is_regexp=False)
    assert value == 'value'

def test_get_value_with_no_option(ini_lookup, tmp_path):
    # Setup the ini file
    ini_file = tmp_path / "test.ini"
    ini_file.write_text("[section1]\nkey=value\n")

    # Read the ini file with configparser
    ini_lookup.cp.read(str(ini_file))

    # Test get_value with no option
    value = ini_lookup.get_value('no_such_key', 'section1', 'default', is_regexp=False)
    assert value == 'default'
