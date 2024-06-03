# file lib/ansible/modules/apt_repository.py:280-289
# lines [280, 281, 285, 286, 287, 288, 289]
# branches []

import pytest
from unittest import mock

# Assuming the SourcesList class is imported from ansible.modules.apt_repository
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def mock_apt_pkg(mocker):
    apt_pkg_mock = mocker.patch('ansible.modules.apt_repository.apt_pkg')
    return apt_pkg_mock

def test_apt_cfg_file_with_find_file(mock_apt_pkg):
    # Mock the find_file method to simulate its presence
    mock_apt_pkg.config.find_file.return_value = '/mock/path'
    
    result = SourcesList._apt_cfg_file('test_file')
    
    mock_apt_pkg.config.find_file.assert_called_once_with('test_file')
    assert result == '/mock/path'

def test_apt_cfg_file_with_Config_FindFile(mock_apt_pkg):
    # Remove the find_file method to simulate its absence
    del mock_apt_pkg.config.find_file
    mock_apt_pkg.Config.FindFile.return_value = '/mock/path'
    
    result = SourcesList._apt_cfg_file('test_file')
    
    mock_apt_pkg.Config.FindFile.assert_called_once_with('test_file')
    assert result == '/mock/path'
