# file: lib/ansible/cli/arguments/option_helpers.py:161-183
# asked: {"lines": [161, 163, 164, 166, 168, 169, 170, 171, 172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183], "branches": [[163, 164], [163, 166], [169, 170], [169, 171], [172, 173], [172, 175]]}
# gained: {"lines": [161, 163, 164, 166, 168, 169, 170, 171, 172, 175, 176, 177, 178, 179, 180, 181, 182, 183], "branches": [[163, 164], [163, 166], [169, 170], [172, 175]]}

import pytest
import sys
from unittest import mock
from jinja2 import __version__ as j2_version
import ansible
from ansible import constants as C
from ansible.module_utils.common.yaml import HAS_LIBYAML
from ansible.release import __version__
from ansible.cli.arguments.option_helpers import version

@pytest.fixture
def mock_gitinfo(monkeypatch):
    def mock_gitinfo():
        return "mocked_git_info"
    monkeypatch.setattr('ansible.cli.arguments.option_helpers._gitinfo', mock_gitinfo)

def test_version_with_prog(mock_gitinfo):
    prog = "ansible"
    result = version(prog)
    assert prog in result
    assert "core" in result
    assert __version__ in result
    assert "mocked_git_info" in result
    assert f"config file = {C.CONFIG_FILE}" in result
    assert "configured module search path" in result
    assert "ansible python module location" in result
    assert "ansible collection location" in result
    assert "executable location" in result
    assert "python version" in result
    assert f"jinja version = {j2_version}" in result
    assert f"libyaml = {HAS_LIBYAML}" in result

def test_version_without_prog(mock_gitinfo):
    result = version()
    assert __version__ in result
    assert "mocked_git_info" in result
    assert f"config file = {C.CONFIG_FILE}" in result
    assert "configured module search path" in result
    assert "ansible python module location" in result
    assert "ansible collection location" in result
    assert "executable location" in result
    assert "python version" in result
    assert f"jinja version = {j2_version}" in result
    assert f"libyaml = {HAS_LIBYAML}" in result
