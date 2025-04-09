# file: lib/ansible/cli/arguments/option_helpers.py:161-183
# asked: {"lines": [], "branches": [[169, 171]]}
# gained: {"lines": [], "branches": [[169, 171]]}

import pytest
import sys
import ansible
from ansible.cli.arguments.option_helpers import version
from unittest.mock import patch

@pytest.fixture
def mock_constants(monkeypatch):
    class MockConstants:
        CONFIG_FILE = "/path/to/config"
        DEFAULT_MODULE_PATH = "/path/to/modules"
        COLLECTIONS_PATHS = ["/path/to/collections"]
    
    monkeypatch.setattr("ansible.cli.arguments.option_helpers.C", MockConstants)
    monkeypatch.setattr("ansible.cli.arguments.option_helpers.__version__", "2.9.10")
    monkeypatch.setattr("ansible.cli.arguments.option_helpers.j2_version", "2.11.3")
    monkeypatch.setattr("ansible.cli.arguments.option_helpers.HAS_LIBYAML", True)

@pytest.fixture
def mock_gitinfo(monkeypatch):
    def mock_gitinfo():
        return "gitinfo"
    monkeypatch.setattr("ansible.cli.arguments.option_helpers._gitinfo", mock_gitinfo)

def test_version_with_prog(mock_constants, mock_gitinfo):
    result = version(prog="ansible")
    assert "ansible [core 2.9.10] gitinfo" in result
    assert "config file = /path/to/config" in result
    assert "configured module search path = /path/to/modules" in result
    assert "ansible python module location = " in result
    assert "ansible collection location = /path/to/collections" in result
    assert "executable location = " in result
    assert "python version = " in result
    assert "jinja version = 2.11.3" in result
    assert "libyaml = True" in result

def test_version_without_prog(mock_constants, mock_gitinfo):
    result = version()
    assert "2.9.10 gitinfo" in result
    assert "config file = /path/to/config" in result
    assert "configured module search path = /path/to/modules" in result
    assert "ansible python module location = " in result
    assert "ansible collection location = /path/to/collections" in result
    assert "executable location = " in result
    assert "python version = " in result
    assert "jinja version = 2.11.3" in result
    assert "libyaml = True" in result

def test_version_without_gitinfo(mock_constants, monkeypatch):
    def mock_gitinfo():
        return None
    monkeypatch.setattr("ansible.cli.arguments.option_helpers._gitinfo", mock_gitinfo)
    
    result = version(prog="ansible")
    assert "ansible [core 2.9.10]" in result
    assert "config file = /path/to/config" in result
    assert "configured module search path = /path/to/modules" in result
    assert "ansible python module location = " in result
    assert "ansible collection location = /path/to/collections" in result
    assert "executable location = " in result
    assert "python version = " in result
    assert "jinja version = 2.11.3" in result
    assert "libyaml = True" in result

def test_version_with_default_module_path_none(mock_constants, monkeypatch):
    class MockConstants:
        CONFIG_FILE = "/path/to/config"
        DEFAULT_MODULE_PATH = None
        COLLECTIONS_PATHS = ["/path/to/collections"]
    
    monkeypatch.setattr("ansible.cli.arguments.option_helpers.C", MockConstants)
    
    result = version(prog="ansible")
    assert "configured module search path = Default w/o overrides" in result
