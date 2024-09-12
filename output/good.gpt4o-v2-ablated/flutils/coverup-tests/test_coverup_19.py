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
    
    result = _get_name(parser, 'setup.cfg')
    assert result == 'test_name'

def test_get_name_no_section(monkeypatch):
    parser = ConfigParser()
    
    with pytest.raises(LookupError) as excinfo:
        _get_name(parser, 'setup.cfg')
    assert "The config file, 'setup.cfg', is missing the 'metadata' section." in str(excinfo.value)

def test_get_name_no_option(monkeypatch):
    parser = ConfigParser()
    parser.add_section('metadata')
    
    with pytest.raises(LookupError) as excinfo:
        _get_name(parser, 'setup.cfg')
    assert "The 'metadata', section is missing the 'name' option in the config file, 'setup.cfg'." in str(excinfo.value)

def test_get_name_empty_option(monkeypatch):
    parser = ConfigParser()
    parser.add_section('metadata')
    parser.set('metadata', 'name', '')
    
    with pytest.raises(LookupError) as excinfo:
        _get_name(parser, 'setup.cfg')
    assert "The 'metadata', section's, 'name' option is not set in the config file, 'setup.cfg'." in str(excinfo.value)
