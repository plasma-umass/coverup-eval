# file: lib/ansible/cli/arguments/option_helpers.py:161-183
# asked: {"lines": [161, 163, 164, 166, 168, 169, 170, 171, 172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183], "branches": [[163, 164], [163, 166], [169, 170], [169, 171], [172, 173], [172, 175]]}
# gained: {"lines": [161, 163, 164, 166, 168, 169, 170, 171, 172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183], "branches": [[163, 164], [163, 166], [169, 170], [172, 173], [172, 175]]}

import pytest
import sys
import ansible
from ansible.cli.arguments.option_helpers import version
from unittest.mock import patch

@pytest.fixture
def mock_constants(monkeypatch):
    class MockConstants:
        CONFIG_FILE = "/etc/ansible/ansible.cfg"
        DEFAULT_MODULE_PATH = "/usr/share/ansible"
        COLLECTIONS_PATHS = ["/usr/share/ansible/collections"]
    
    monkeypatch.setattr("ansible.cli.arguments.option_helpers.C", MockConstants)
    monkeypatch.setattr("ansible.cli.arguments.option_helpers.__version__", "2.9.10")
    monkeypatch.setattr("ansible.cli.arguments.option_helpers.j2_version", "2.11.2")
    monkeypatch.setattr("ansible.cli.arguments.option_helpers.HAS_LIBYAML", True)

@pytest.fixture
def mock_gitinfo(monkeypatch):
    def mock_gitinfo():
        return "gitinfo"
    monkeypatch.setattr("ansible.cli.arguments.option_helpers._gitinfo", mock_gitinfo)

def test_version_with_prog(mock_constants, mock_gitinfo):
    result = version(prog="ansible")
    assert "ansible [core 2.9.10] gitinfo" in result
    assert "config file = /etc/ansible/ansible.cfg" in result
    assert "configured module search path = /usr/share/ansible" in result
    assert "ansible python module location = %s" % ':'.join(ansible.__path__) in result
    assert "ansible collection location = /usr/share/ansible/collections" in result
    assert "executable location = %s" % sys.argv[0] in result
    assert "python version = %s" % ''.join(sys.version.splitlines()) in result
    assert "jinja version = 2.11.2" in result
    assert "libyaml = True" in result

def test_version_without_prog(mock_constants, mock_gitinfo):
    result = version()
    assert "2.9.10 gitinfo" in result
    assert "config file = /etc/ansible/ansible.cfg" in result
    assert "configured module search path = /usr/share/ansible" in result
    assert "ansible python module location = %s" % ':'.join(ansible.__path__) in result
    assert "ansible collection location = /usr/share/ansible/collections" in result
    assert "executable location = %s" % sys.argv[0] in result
    assert "python version = %s" % ''.join(sys.version.splitlines()) in result
    assert "jinja version = 2.11.2" in result
    assert "libyaml = True" in result

def test_version_with_default_module_path_none(mock_constants, mock_gitinfo, monkeypatch):
    monkeypatch.setattr("ansible.cli.arguments.option_helpers.C.DEFAULT_MODULE_PATH", None)
    result = version()
    assert "configured module search path = Default w/o overrides" in result
