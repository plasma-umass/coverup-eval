# file lib/ansible/plugins/loader.py:1132-1145
# lines [1132, 1133, 1134, 1136, 1137, 1138, 1140, 1143, 1145]
# branches ['1133->1134', '1133->1136', '1136->1137', '1136->1140']

import pytest
from ansible.plugins.loader import _does_collection_support_ansible_version
from packaging.specifiers import SpecifierSet
from packaging.version import Version
from ansible.utils.display import Display

# Mock the display object to capture warnings
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'warning')

# Test when requirement_string is None
def test_does_collection_support_ansible_version_no_requirement(mock_display):
    assert _does_collection_support_ansible_version(None, '2.9.10') is True
    mock_display.assert_not_called()

# Test when SpecifierSet is None (simulate packaging module not available)
def test_does_collection_support_ansible_version_no_specifierset(mocker, mock_display):
    mocker.patch('ansible.plugins.loader.SpecifierSet', None)
    assert _does_collection_support_ansible_version('>=2.9', '2.9.10') is True
    mock_display.assert_called_once_with('packaging Python module unavailable; unable to validate collection Ansible version requirements')

# Test when requirement_string is a valid specifier and ansible_version is contained within it
def test_does_collection_support_ansible_version_valid_requirement(mock_display):
    assert _does_collection_support_ansible_version('>=2.9, <3.0', '2.9.10') is True
    mock_display.assert_not_called()

# Test when requirement_string is a valid specifier and ansible_version is not contained within it
def test_does_collection_support_ansible_version_invalid_requirement(mock_display):
    assert _does_collection_support_ansible_version('>=2.9, <3.0', '3.0.1') is False
    mock_display.assert_not_called()

# Test when ansible_version is a pre-release version
def test_does_collection_support_ansible_version_prerelease_version(mock_display):
    assert _does_collection_support_ansible_version('>=2.9, <3.0', '3.0.0b1') is False
    mock_display.assert_not_called()
