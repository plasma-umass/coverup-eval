# file: lib/ansible/cli/arguments/option_helpers.py:161-183
# asked: {"lines": [173], "branches": [[172, 173]]}
# gained: {"lines": [173], "branches": [[172, 173]]}

import pytest
from unittest import mock
import sys
from jinja2 import __version__ as j2_version
import ansible
from ansible import constants as C
from ansible.module_utils.common.yaml import HAS_LIBYAML
from ansible.release import __version__
from ansible.cli.arguments.option_helpers import version

@pytest.fixture
def mock_constants(monkeypatch):
    class MockConstants:
        CONFIG_FILE = "/path/to/config"
        DEFAULT_MODULE_PATH = None
        COLLECTIONS_PATHS = ["/path/to/collections"]

    monkeypatch.setattr("ansible.constants", MockConstants)

def test_version_with_prog(mock_constants, monkeypatch):
    prog = "ansible-playbook"
    monkeypatch.setattr(C, 'DEFAULT_MODULE_PATH', None)
    result = version(prog)
    assert "ansible-playbook [core" in result
    assert "Default w/o overrides" in result

def test_version_without_prog(mock_constants, monkeypatch):
    monkeypatch.setattr(C, 'DEFAULT_MODULE_PATH', None)
    result = version()
    assert __version__ in result
    assert "Default w/o overrides" in result

def test_version_with_default_module_path(mock_constants, monkeypatch):
    monkeypatch.setattr(C, 'DEFAULT_MODULE_PATH', "/custom/module/path")
    result = version()
    assert "/custom/module/path" in result
