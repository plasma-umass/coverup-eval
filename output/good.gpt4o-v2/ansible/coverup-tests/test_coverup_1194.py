# file: lib/ansible/plugins/loader.py:1132-1145
# asked: {"lines": [1136, 1137, 1138, 1140, 1143, 1145], "branches": [[1133, 1136], [1136, 1137], [1136, 1140]]}
# gained: {"lines": [1136, 1137, 1138, 1140, 1143, 1145], "branches": [[1133, 1136], [1136, 1137], [1136, 1140]]}

import pytest
from unittest.mock import patch
from ansible.plugins.loader import _does_collection_support_ansible_version
from packaging.specifiers import SpecifierSet
from packaging.version import Version

def test_no_requirement_string():
    assert _does_collection_support_ansible_version("", "2.9.10") == True

def test_no_specifier_set(monkeypatch):
    with patch('ansible.plugins.loader.SpecifierSet', None):
        with patch('ansible.plugins.loader.display.warning') as mock_warning:
            assert _does_collection_support_ansible_version(">=2.9.0", "2.9.10") == True
            mock_warning.assert_called_once_with('packaging Python module unavailable; unable to validate collection Ansible version requirements')

def test_valid_requirement_string():
    requirement_string = ">=2.9.0"
    ansible_version = "2.9.10"
    assert _does_collection_support_ansible_version(requirement_string, ansible_version) == True

def test_invalid_requirement_string():
    requirement_string = ">=2.10.0"
    ansible_version = "2.9.10"
    assert _does_collection_support_ansible_version(requirement_string, ansible_version) == False
