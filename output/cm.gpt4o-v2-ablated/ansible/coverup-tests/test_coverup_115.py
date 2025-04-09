# file: lib/ansible/plugins/loader.py:1132-1145
# asked: {"lines": [1132, 1133, 1134, 1136, 1137, 1138, 1140, 1143, 1145], "branches": [[1133, 1134], [1133, 1136], [1136, 1137], [1136, 1140]]}
# gained: {"lines": [1132, 1133, 1134, 1136, 1137, 1138, 1140, 1143, 1145], "branches": [[1133, 1134], [1133, 1136], [1136, 1137], [1136, 1140]]}

import pytest
from ansible.plugins.loader import _does_collection_support_ansible_version
from packaging.specifiers import SpecifierSet
from packaging.version import Version
from unittest.mock import patch

@pytest.fixture(autouse=True)
def mock_display_warning(monkeypatch):
    from ansible.utils.display import Display
    display = Display()
    monkeypatch.setattr('ansible.plugins.loader.display', display)
    return display

def test_no_requirement_string():
    assert _does_collection_support_ansible_version('', '2.9.10') == True

def test_no_specifier_set(monkeypatch):
    monkeypatch.setattr('ansible.plugins.loader.SpecifierSet', None)
    with patch('ansible.plugins.loader.display.warning') as mock_warning:
        assert _does_collection_support_ansible_version('>=2.9', '2.9.10') == True
        mock_warning.assert_called_once_with('packaging Python module unavailable; unable to validate collection Ansible version requirements')

def test_version_supported():
    assert _does_collection_support_ansible_version('>=2.9', '2.9.10') == True

def test_version_not_supported():
    assert _does_collection_support_ansible_version('>=2.10', '2.9.10') == False

def test_ignore_prerelease_postrelease_beta_dev_flags():
    assert _does_collection_support_ansible_version('>=2.9', '2.9.10.dev0') == True
    assert _does_collection_support_ansible_version('>=2.9', '2.9.10.post1') == True
    assert _does_collection_support_ansible_version('>=2.9', '2.9.10a1') == True
    assert _does_collection_support_ansible_version('>=2.9', '2.9.10b1') == True
