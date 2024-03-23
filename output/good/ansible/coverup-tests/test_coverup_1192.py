# file lib/ansible/module_utils/common/sys_info.py:82-109
# lines [94, 95, 97, 98, 100, 101, 102, 104, 105, 106, 107]
# branches ['90->94', '97->98', '97->100', '100->101', '100->104', '104->105', '104->109', '106->107', '106->109']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.common.sys_info import get_distribution_codename

@pytest.fixture
def mock_platform_system(mocker):
    return mocker.patch('platform.system')

@pytest.fixture
def mock_distro(mocker):
    mocker.patch('ansible.module_utils.common.sys_info.distro.os_release_info', return_value={})
    mocker.patch('ansible.module_utils.common.sys_info.distro.id', return_value='')
    mocker.patch('ansible.module_utils.common.sys_info.distro.lsb_release_info', return_value={})
    mocker.patch('ansible.module_utils.common.sys_info.distro.codename', return_value='')
    return mocker

def test_get_distribution_codename_non_linux(mock_platform_system):
    mock_platform_system.return_value = 'NonLinux'
    assert get_distribution_codename() is None

def test_get_distribution_codename_no_codename(mock_platform_system, mock_distro):
    mock_platform_system.return_value = 'Linux'
    assert get_distribution_codename() is None

def test_get_distribution_codename_with_version_codename(mock_platform_system, mock_distro):
    mock_platform_system.return_value = 'Linux'
    mock_distro.patch('ansible.module_utils.common.sys_info.distro.os_release_info', return_value={'version_codename': 'focal'})
    assert get_distribution_codename() == 'focal'

def test_get_distribution_codename_with_ubuntu_codename(mock_platform_system, mock_distro):
    mock_platform_system.return_value = 'Linux'
    mock_distro.patch('ansible.module_utils.common.sys_info.distro.os_release_info', return_value={'ubuntu_codename': 'bionic'})
    assert get_distribution_codename() == 'bionic'

def test_get_distribution_codename_with_lsb_codename(mock_platform_system, mock_distro):
    mock_platform_system.return_value = 'Linux'
    mock_distro.patch('ansible.module_utils.common.sys_info.distro.id', return_value='ubuntu')
    mock_distro.patch('ansible.module_utils.common.sys_info.distro.lsb_release_info', return_value={'codename': 'xenial'})
    assert get_distribution_codename() == 'xenial'

def test_get_distribution_codename_with_empty_codename(mock_platform_system, mock_distro):
    mock_platform_system.return_value = 'Linux'
    mock_distro.patch('ansible.module_utils.common.sys_info.distro.codename', return_value='')
    assert get_distribution_codename() is None
