# file lib/ansible/plugins/loader.py:1132-1145
# lines [1136, 1137, 1138, 1140, 1143, 1145]
# branches ['1133->1136', '1136->1137', '1136->1140']

import pytest
from unittest import mock
from ansible.plugins.loader import _does_collection_support_ansible_version

def test_does_collection_support_ansible_version_no_requirement_string():
    assert _does_collection_support_ansible_version("", "2.9.10") == True

def test_does_collection_support_ansible_version_no_specifierset(mocker):
    mocker.patch('ansible.plugins.loader.SpecifierSet', None)
    mock_display_warning = mocker.patch('ansible.plugins.loader.display.warning')
    
    result = _does_collection_support_ansible_version(">=2.9.0", "2.9.10")
    
    mock_display_warning.assert_called_once_with('packaging Python module unavailable; unable to validate collection Ansible version requirements')
    assert result == True

def test_does_collection_support_ansible_version_valid_requirement(mocker):
    from packaging.specifiers import SpecifierSet
    from packaging.version import Version

    mocker.patch('ansible.plugins.loader.SpecifierSet', SpecifierSet)
    mocker.patch('ansible.plugins.loader.Version', Version)
    
    requirement_string = ">=2.9.0"
    ansible_version = "2.9.10"
    
    result = _does_collection_support_ansible_version(requirement_string, ansible_version)
    
    ss = SpecifierSet(requirement_string)
    base_ansible_version = Version(ansible_version).base_version
    
    assert result == ss.contains(base_ansible_version)
