# file lib/ansible/modules/apt_repository.py:196-209
# lines [196, 197, 198, 200, 201, 204, 205, 208, 209]
# branches ['204->205', '204->208', '208->exit', '208->209']

import os
import glob
import pytest
from unittest import mock

# Assuming the SourcesList class is imported from ansible.modules.apt_repository
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def mock_apt_cfg_file(mocker):
    mocker.patch('ansible.modules.apt_repository.SourcesList._apt_cfg_file', side_effect=lambda x: '/etc/apt/sources.list')
    mocker.patch('ansible.modules.apt_repository.SourcesList._apt_cfg_dir', side_effect=lambda x: '/etc/apt/sources.list.d')

@pytest.fixture
def mock_filesystem(mocker):
    mocker.patch('os.path.isfile', return_value=True)
    mocker.patch('glob.iglob', return_value=['/etc/apt/sources.list.d/example.list'])

@pytest.fixture
def mock_load(mocker):
    return mocker.patch('ansible.modules.apt_repository.SourcesList.load')

def test_sources_list_initialization(mock_apt_cfg_file, mock_filesystem, mock_load):
    module = mock.Mock()
    sources_list = SourcesList(module)
    
    # Assertions to verify the correct files are being loaded
    mock_load.assert_any_call('/etc/apt/sources.list')
    mock_load.assert_any_call('/etc/apt/sources.list.d/example.list')
    
    # Verify that the files dictionary is populated correctly
    assert sources_list.files == {}
    
    # Verify that new_repos is an empty set
    assert sources_list.new_repos == set()
    
    # Verify that default_file is set correctly
    assert sources_list.default_file == '/etc/apt/sources.list'
