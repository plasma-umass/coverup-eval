# file: lib/ansible/module_utils/common/sys_info.py:41-79
# asked: {"lines": [41, 50, 52, 57, 58, 60, 61, 62, 67, 68, 73, 74, 77, 79], "branches": [[60, 61], [60, 77], [61, 62], [61, 79], [67, 68], [67, 73], [73, 74], [73, 79]]}
# gained: {"lines": [41, 50, 52, 57, 58, 60, 61, 62, 67, 68, 73, 74, 77, 79], "branches": [[60, 61], [60, 77], [61, 62], [61, 79], [67, 68], [67, 73], [73, 74], [73, 79]]}

import pytest
from unittest.mock import patch
from ansible.module_utils.common.sys_info import get_distribution_version

@pytest.fixture
def mock_distro_version():
    with patch('ansible.module_utils.distro.version') as mock_version:
        yield mock_version

@pytest.fixture
def mock_distro_id():
    with patch('ansible.module_utils.distro.id') as mock_id:
        yield mock_id

def test_get_distribution_version_centos(mock_distro_version, mock_distro_id):
    mock_distro_version.side_effect = ['7.9.2009', '7.9.2009']
    mock_distro_id.return_value = 'centos'
    
    version = get_distribution_version()
    
    assert version == '7.9'
    mock_distro_version.assert_called_with(best=True)
    mock_distro_id.assert_called_once()

def test_get_distribution_version_debian(mock_distro_version, mock_distro_id):
    mock_distro_version.side_effect = ['10', '10.7']
    mock_distro_id.return_value = 'debian'
    
    version = get_distribution_version()
    
    assert version == '10.7'
    mock_distro_version.assert_called_with(best=True)
    mock_distro_id.assert_called_once()

def test_get_distribution_version_other(mock_distro_version, mock_distro_id):
    mock_distro_version.return_value = '20.04'
    mock_distro_id.return_value = 'ubuntu'
    
    version = get_distribution_version()
    
    assert version == '20.04'
    mock_distro_version.assert_called_once_with()
    mock_distro_id.assert_called_once()

def test_get_distribution_version_none(mock_distro_version, mock_distro_id):
    mock_distro_version.return_value = None
    mock_distro_id.return_value = 'ubuntu'
    
    version = get_distribution_version()
    
    assert version == ''
    mock_distro_version.assert_called_once_with()
    mock_distro_id.assert_called_once()
