# file: lib/ansible/cli/arguments/option_helpers.py:161-183
# asked: {"lines": [161, 163, 164, 166, 168, 169, 170, 171, 172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183], "branches": [[163, 164], [163, 166], [169, 170], [169, 171], [172, 173], [172, 175]]}
# gained: {"lines": [161, 163, 164, 166, 168, 169, 170, 171, 172, 175, 176, 177, 178, 179, 180, 181, 182, 183], "branches": [[163, 164], [163, 166], [169, 170], [169, 171], [172, 175]]}

import pytest
import sys
from unittest import mock
from ansible.cli.arguments.option_helpers import version

@pytest.fixture
def mock_gitinfo(monkeypatch):
    def mock_gitinfo():
        return "mocked_git_info"
    monkeypatch.setattr('ansible.cli.arguments.option_helpers._gitinfo', mock_gitinfo)

@pytest.fixture
def mock_constants(monkeypatch):
    class MockConstants:
        CONFIG_FILE = "mocked_config_file"
        DEFAULT_MODULE_PATH = "mocked_module_path"
        COLLECTIONS_PATHS = ["mocked_collection_path"]
    monkeypatch.setattr('ansible.cli.arguments.option_helpers.C', MockConstants)

def test_version_with_prog(mock_gitinfo, mock_constants):
    prog = "ansible"
    result = version(prog)
    assert "ansible [core" in result
    assert "mocked_git_info" in result
    assert "mocked_config_file" in result
    assert "mocked_module_path" in result
    assert "mocked_collection_path" in result
    assert "executable location = " in result
    assert "python version = " in result
    assert "jinja version = " in result
    assert "libyaml = " in result

def test_version_without_prog(mock_gitinfo, mock_constants):
    result = version()
    assert "mocked_git_info" in result
    assert "mocked_config_file" in result
    assert "mocked_module_path" in result
    assert "mocked_collection_path" in result
    assert "executable location = " in result
    assert "python version = " in result
    assert "jinja version = " in result
    assert "libyaml = " in result

def test_version_no_gitinfo(mock_constants, monkeypatch):
    def mock_gitinfo():
        return None
    monkeypatch.setattr('ansible.cli.arguments.option_helpers._gitinfo', mock_gitinfo)
    result = version()
    assert "mocked_config_file" in result
    assert "mocked_module_path" in result
    assert "mocked_collection_path" in result
    assert "executable location = " in result
    assert "python version = " in result
    assert "jinja version = " in result
    assert "libyaml = " in result
