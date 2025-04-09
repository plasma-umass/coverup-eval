# file: lib/ansible/plugins/loader.py:1132-1145
# asked: {"lines": [1132, 1133, 1134, 1136, 1137, 1138, 1140, 1143, 1145], "branches": [[1133, 1134], [1133, 1136], [1136, 1137], [1136, 1140]]}
# gained: {"lines": [1132, 1133, 1134, 1136, 1137, 1138, 1140, 1143, 1145], "branches": [[1133, 1134], [1133, 1136], [1136, 1137], [1136, 1140]]}

import pytest
from unittest.mock import patch
from ansible.plugins.loader import _does_collection_support_ansible_version
from packaging.specifiers import SpecifierSet
from packaging.version import Version

@pytest.mark.parametrize("requirement_string, ansible_version, expected", [
    ("", "2.9.10", True),  # No requirement string
    (None, "2.9.10", True),  # None as requirement string
    (">=2.9.0", "2.9.10", True),  # Valid requirement string
    (">=2.10.0", "2.9.10", False),  # Version not satisfying the requirement
])
def test_does_collection_support_ansible_version(requirement_string, ansible_version, expected):
    assert _does_collection_support_ansible_version(requirement_string, ansible_version) == expected

def test_does_collection_support_ansible_version_no_specifierset(monkeypatch):
    def mock_specifierset(*args, **kwargs):
        raise ImportError("No module named 'packaging.specifiers'")

    monkeypatch.setattr("ansible.plugins.loader.SpecifierSet", None)
    with patch("ansible.plugins.loader.display.warning") as mock_warning:
        assert _does_collection_support_ansible_version(">=2.9.0", "2.9.10") == True
        mock_warning.assert_called_once_with('packaging Python module unavailable; unable to validate collection Ansible version requirements')

def test_does_collection_support_ansible_version_base_version(monkeypatch):
    class MockVersion:
        def __init__(self, version):
            self.base_version = "2.9.0"

    monkeypatch.setattr("ansible.plugins.loader.Version", MockVersion)
    assert _does_collection_support_ansible_version(">=2.9.0", "2.9.10") == True
