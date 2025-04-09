# file: lib/ansible/module_utils/common/sys_info.py:82-109
# asked: {"lines": [82, 89, 90, 94, 95, 97, 98, 100, 101, 102, 104, 105, 106, 107, 109], "branches": [[90, 94], [90, 109], [97, 98], [97, 100], [100, 101], [100, 104], [104, 105], [104, 109], [106, 107], [106, 109]]}
# gained: {"lines": [82, 89, 90, 94, 95, 97, 98, 100, 101, 102, 104, 105, 106, 107, 109], "branches": [[90, 94], [90, 109], [97, 98], [97, 100], [100, 101], [100, 104], [104, 105], [104, 109], [106, 107], [106, 109]]}

import pytest
import platform
from ansible.module_utils import distro
from ansible.module_utils.common.sys_info import get_distribution_codename

@pytest.fixture
def mock_linux_system(monkeypatch):
    monkeypatch.setattr(platform, 'system', lambda: 'Linux')

@pytest.fixture
def mock_non_linux_system(monkeypatch):
    monkeypatch.setattr(platform, 'system', lambda: 'Windows')

def test_get_distribution_codename_linux_with_version_codename(mock_linux_system, mocker):
    mock_os_release_info = {'version_codename': 'focal'}
    mocker.patch('distro.os_release_info', return_value=mock_os_release_info)
    assert get_distribution_codename() == 'focal'

def test_get_distribution_codename_linux_with_ubuntu_codename(mock_linux_system, mocker):
    mock_os_release_info = {'version_codename': None, 'ubuntu_codename': 'bionic'}
    mocker.patch('distro.os_release_info', return_value=mock_os_release_info)
    assert get_distribution_codename() == 'bionic'

def test_get_distribution_codename_linux_with_lsb_release_info(mock_linux_system, mocker):
    mock_os_release_info = {'version_codename': None, 'ubuntu_codename': None}
    mock_lsb_release_info = {'codename': 'xenial'}
    mocker.patch('distro.os_release_info', return_value=mock_os_release_info)
    mocker.patch('distro.id', return_value='ubuntu')
    mocker.patch('distro.lsb_release_info', return_value=mock_lsb_release_info)
    assert get_distribution_codename() == 'xenial'

def test_get_distribution_codename_linux_with_distro_codename(mock_linux_system, mocker):
    mock_os_release_info = {'version_codename': None, 'ubuntu_codename': None}
    mocker.patch('distro.os_release_info', return_value=mock_os_release_info)
    mocker.patch('distro.id', return_value='fedora')
    mocker.patch('distro.codename', return_value='twenty-eight')
    assert get_distribution_codename() == 'twenty-eight'

def test_get_distribution_codename_linux_with_empty_distro_codename(mock_linux_system, mocker):
    mock_os_release_info = {'version_codename': None, 'ubuntu_codename': None}
    mocker.patch('distro.os_release_info', return_value=mock_os_release_info)
    mocker.patch('distro.id', return_value='fedora')
    mocker.patch('distro.codename', return_value='')
    assert get_distribution_codename() is None

def test_get_distribution_codename_non_linux(mock_non_linux_system):
    assert get_distribution_codename() is None
