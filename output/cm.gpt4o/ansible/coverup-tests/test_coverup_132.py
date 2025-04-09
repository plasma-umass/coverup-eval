# file lib/ansible/module_utils/common/sys_info.py:82-109
# lines [82, 89, 90, 94, 95, 97, 98, 100, 101, 102, 104, 105, 106, 107, 109]
# branches ['90->94', '90->109', '97->98', '97->100', '100->101', '100->104', '104->105', '104->109', '106->107', '106->109']

import pytest
import platform
from unittest import mock
from ansible.module_utils.common.sys_info import get_distribution_codename

@pytest.fixture
def mock_distro(mocker):
    mock_distro = mocker.patch('ansible.module_utils.common.sys_info.distro')
    return mock_distro

def test_get_distribution_codename_linux_with_version_codename(mock_distro):
    mock_distro.os_release_info.return_value = {'version_codename': 'focal'}
    mock_distro.id.return_value = 'ubuntu'
    mock_distro.lsb_release_info.return_value = {'codename': 'focal'}
    mock_distro.codename.return_value = 'focal'

    with mock.patch('platform.system', return_value='Linux'):
        assert get_distribution_codename() == 'focal'

def test_get_distribution_codename_linux_with_ubuntu_codename(mock_distro):
    mock_distro.os_release_info.return_value = {'version_codename': None, 'ubuntu_codename': 'bionic'}
    mock_distro.id.return_value = 'ubuntu'
    mock_distro.lsb_release_info.return_value = {'codename': 'bionic'}
    mock_distro.codename.return_value = 'bionic'

    with mock.patch('platform.system', return_value='Linux'):
        assert get_distribution_codename() == 'bionic'

def test_get_distribution_codename_linux_with_lsb_release_info(mock_distro):
    mock_distro.os_release_info.return_value = {'version_codename': None, 'ubuntu_codename': None}
    mock_distro.id.return_value = 'ubuntu'
    mock_distro.lsb_release_info.return_value = {'codename': 'xenial'}
    mock_distro.codename.return_value = 'xenial'

    with mock.patch('platform.system', return_value='Linux'):
        assert get_distribution_codename() == 'xenial'

def test_get_distribution_codename_linux_with_distro_codename(mock_distro):
    mock_distro.os_release_info.return_value = {'version_codename': None, 'ubuntu_codename': None}
    mock_distro.id.return_value = 'fedora'
    mock_distro.lsb_release_info.return_value = {'codename': None}
    mock_distro.codename.return_value = 'twenty-eight'

    with mock.patch('platform.system', return_value='Linux'):
        assert get_distribution_codename() == 'twenty-eight'

def test_get_distribution_codename_linux_with_empty_distro_codename(mock_distro):
    mock_distro.os_release_info.return_value = {'version_codename': None, 'ubuntu_codename': None}
    mock_distro.id.return_value = 'fedora'
    mock_distro.lsb_release_info.return_value = {'codename': None}
    mock_distro.codename.return_value = ''

    with mock.patch('platform.system', return_value='Linux'):
        assert get_distribution_codename() is None

def test_get_distribution_codename_non_linux():
    with mock.patch('platform.system', return_value='Windows'):
        assert get_distribution_codename() is None
