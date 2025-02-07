# file: lib/ansible/module_utils/common/sys_info.py:82-109
# asked: {"lines": [82, 89, 90, 94, 95, 97, 98, 100, 101, 102, 104, 105, 106, 107, 109], "branches": [[90, 94], [90, 109], [97, 98], [97, 100], [100, 101], [100, 104], [104, 105], [104, 109], [106, 107], [106, 109]]}
# gained: {"lines": [82, 89, 90, 94, 95, 97, 98, 100, 101, 102, 104, 105, 106, 107, 109], "branches": [[90, 94], [90, 109], [97, 98], [97, 100], [100, 101], [100, 104], [104, 105], [104, 109], [106, 107], [106, 109]]}

import pytest
import platform
from unittest.mock import patch, MagicMock
from ansible.module_utils.common.sys_info import get_distribution_codename

@pytest.fixture
def mock_platform_system():
    with patch('platform.system') as mock:
        yield mock

@pytest.fixture
def mock_distro_os_release_info():
    with patch('distro.os_release_info') as mock:
        yield mock

@pytest.fixture
def mock_distro_lsb_release_info():
    with patch('distro.lsb_release_info') as mock:
        yield mock

@pytest.fixture
def mock_distro_id():
    with patch('distro.id') as mock:
        yield mock

@pytest.fixture
def mock_distro_codename():
    with patch('distro.codename') as mock:
        yield mock

def test_get_distribution_codename_linux_with_version_codename(mock_platform_system, mock_distro_os_release_info):
    mock_platform_system.return_value = 'Linux'
    mock_distro_os_release_info.return_value = {'version_codename': 'focal'}
    
    codename = get_distribution_codename()
    
    assert codename == 'focal'

def test_get_distribution_codename_linux_with_ubuntu_codename(mock_platform_system, mock_distro_os_release_info):
    mock_platform_system.return_value = 'Linux'
    mock_distro_os_release_info.return_value = {'version_codename': None, 'ubuntu_codename': 'bionic'}
    
    codename = get_distribution_codename()
    
    assert codename == 'bionic'

def test_get_distribution_codename_linux_with_lsb_release_info(mock_platform_system, mock_distro_os_release_info, mock_distro_id, mock_distro_lsb_release_info):
    mock_platform_system.return_value = 'Linux'
    mock_distro_os_release_info.return_value = {'version_codename': None, 'ubuntu_codename': None}
    mock_distro_id.return_value = 'ubuntu'
    mock_distro_lsb_release_info.return_value = {'codename': 'xenial'}
    
    codename = get_distribution_codename()
    
    assert codename == 'xenial'

def test_get_distribution_codename_linux_with_distro_codename(mock_platform_system, mock_distro_os_release_info, mock_distro_codename):
    mock_platform_system.return_value = 'Linux'
    mock_distro_os_release_info.return_value = {'version_codename': None, 'ubuntu_codename': None}
    mock_distro_codename.return_value = 'buster'
    
    codename = get_distribution_codename()
    
    assert codename == 'buster'

def test_get_distribution_codename_linux_with_empty_distro_codename(mock_platform_system, mock_distro_os_release_info, mock_distro_codename):
    mock_platform_system.return_value = 'Linux'
    mock_distro_os_release_info.return_value = {'version_codename': None, 'ubuntu_codename': None}
    mock_distro_codename.return_value = ''
    
    codename = get_distribution_codename()
    
    assert codename is None

def test_get_distribution_codename_non_linux(mock_platform_system):
    mock_platform_system.return_value = 'Windows'
    
    codename = get_distribution_codename()
    
    assert codename is None
