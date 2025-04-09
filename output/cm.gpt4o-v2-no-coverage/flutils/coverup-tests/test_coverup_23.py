# file: flutils/setuputils/cfg.py:82-105
# asked: {"lines": [82, 86, 87, 88, 89, 90, 91, 93, 94, 95, 97, 99, 100, 101, 103, 105], "branches": [[99, 100], [99, 105]]}
# gained: {"lines": [82, 86, 87, 88, 89, 90, 91, 93, 94, 95, 97, 99, 100, 101, 103, 105], "branches": [[99, 100], [99, 105]]}

import pytest
from configparser import ConfigParser, NoOptionError, NoSectionError
from flutils.setuputils.cfg import _get_name

def test_get_name_success(monkeypatch):
    config_data = "[metadata]\nname = test_name"
    parser = ConfigParser()
    parser.read_string(config_data)
    
    result = _get_name(parser, "dummy_path")
    assert result == "test_name"

def test_get_name_no_section(monkeypatch):
    config_data = "[no_metadata]\nname = test_name"
    parser = ConfigParser()
    parser.read_string(config_data)
    
    with pytest.raises(LookupError, match="The config file, 'dummy_path', is missing the 'metadata' section."):
        _get_name(parser, "dummy_path")

def test_get_name_no_option(monkeypatch):
    config_data = "[metadata]\nno_name = test_name"
    parser = ConfigParser()
    parser.read_string(config_data)
    
    with pytest.raises(LookupError, match="The 'metadata', section is missing the 'name' option in the config file, 'dummy_path'."):
        _get_name(parser, "dummy_path")

def test_get_name_empty_option(monkeypatch):
    config_data = "[metadata]\nname ="
    parser = ConfigParser()
    parser.read_string(config_data)
    
    with pytest.raises(LookupError, match="The 'metadata', section's, 'name' option is not set in the config file, 'dummy_path'."):
        _get_name(parser, "dummy_path")
