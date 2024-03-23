# file lib/ansible/config/manager.py:187-195
# lines [187, 189, 190, 191, 192, 193, 194, 195]
# branches ['190->191', '190->195']

import pytest
from configparser import ConfigParser
from ansible.config.manager import get_ini_config_value

@pytest.fixture
def ini_file(tmp_path):
    ini_content = """
    [defaults]
    test_key = test_value
    """
    ini_path = tmp_path / "test.ini"
    ini_path.write_text(ini_content)
    return ini_path

def test_get_ini_config_value_existing_section_and_key(mocker, ini_file):
    parser = ConfigParser()
    parser.read(str(ini_file))
    entry = {'section': 'defaults', 'key': 'test_key'}
    value = get_ini_config_value(parser, entry)
    assert value == 'test_value'

def test_get_ini_config_value_non_existing_section(mocker, ini_file):
    parser = ConfigParser()
    parser.read(str(ini_file))
    entry = {'section': 'non_existing_section', 'key': 'test_key'}
    value = get_ini_config_value(parser, entry)
    assert value is None

def test_get_ini_config_value_non_existing_key(mocker, ini_file):
    parser = ConfigParser()
    parser.read(str(ini_file))
    entry = {'section': 'defaults', 'key': 'non_existing_key'}
    value = get_ini_config_value(parser, entry)
    assert value is None

def test_get_ini_config_value_no_parser():
    entry = {'section': 'defaults', 'key': 'test_key'}
    value = get_ini_config_value(None, entry)
    assert value is None

def test_get_ini_config_value_with_exception(mocker, ini_file):
    parser = ConfigParser()
    parser.read(str(ini_file))
    entry = {'section': 'defaults', 'key': 'test_key'}
    mocker.patch.object(parser, 'get', side_effect=Exception("Test exception"))
    value = get_ini_config_value(parser, entry)
    assert value is None
