# file: flutils/setuputils/cfg.py:82-105
# asked: {"lines": [82, 86, 87, 88, 89, 90, 91, 93, 94, 95, 97, 99, 100, 101, 103, 105], "branches": [[99, 100], [99, 105]]}
# gained: {"lines": [82, 86, 87, 88, 89, 90, 91, 93, 94, 95, 97, 99, 100, 101, 103, 105], "branches": [[99, 100], [99, 105]]}

import pytest
from configparser import ConfigParser, NoSectionError, NoOptionError
from flutils.setuputils.cfg import _get_name

def test_get_name_success(monkeypatch):
    parser = ConfigParser()
    parser.add_section('metadata')
    parser.set('metadata', 'name', 'test_name')
    setup_cfg_path = 'dummy_path'
    
    result = _get_name(parser, setup_cfg_path)
    
    assert result == 'test_name'

def test_get_name_no_section_error(monkeypatch):
    parser = ConfigParser()
    setup_cfg_path = 'dummy_path'
    
    with pytest.raises(LookupError) as excinfo:
        _get_name(parser, setup_cfg_path)
    
    assert str(excinfo.value) == "The config file, 'dummy_path', is missing the 'metadata' section."

def test_get_name_no_option_error(monkeypatch):
    parser = ConfigParser()
    parser.add_section('metadata')
    setup_cfg_path = 'dummy_path'
    
    with pytest.raises(LookupError) as excinfo:
        _get_name(parser, setup_cfg_path)
    
    assert str(excinfo.value) == "The 'metadata', section is missing the 'name' option in the config file, 'dummy_path'."

def test_get_name_empty_value_error(monkeypatch):
    parser = ConfigParser()
    parser.add_section('metadata')
    parser.set('metadata', 'name', '')
    setup_cfg_path = 'dummy_path'
    
    with pytest.raises(LookupError) as excinfo:
        _get_name(parser, setup_cfg_path)
    
    assert str(excinfo.value) == "The 'metadata', section's, 'name' option is not set in the config file, 'dummy_path'."
