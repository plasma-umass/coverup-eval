# file: lib/ansible/module_utils/common/sys_info.py:82-109
# asked: {"lines": [89, 90, 94, 95, 97, 98, 100, 101, 102, 104, 105, 106, 107, 109], "branches": [[90, 94], [90, 109], [97, 98], [97, 100], [100, 101], [100, 104], [104, 105], [104, 109], [106, 107], [106, 109]]}
# gained: {"lines": [89, 90, 94, 95, 97, 98, 100, 101, 102, 104, 105, 106, 107, 109], "branches": [[90, 94], [90, 109], [97, 98], [97, 100], [100, 101], [100, 104], [104, 105], [104, 109], [106, 107], [106, 109]]}

import pytest
import platform
from unittest import mock
import distro
from ansible.module_utils.common.sys_info import get_distribution_codename

@pytest.fixture
def mock_platform_linux(monkeypatch):
    monkeypatch.setattr(platform, 'system', lambda: 'Linux')

@pytest.fixture
def mock_platform_non_linux(monkeypatch):
    monkeypatch.setattr(platform, 'system', lambda: 'Windows')

def test_get_distribution_codename_non_linux(mock_platform_non_linux):
    assert get_distribution_codename() is None

def test_get_distribution_codename_linux_no_codename(mock_platform_linux, monkeypatch):
    mock_os_release_info = {
        'version_codename': None,
        'ubuntu_codename': None
    }
    monkeypatch.setattr(distro, 'os_release_info', lambda: mock_os_release_info)
    monkeypatch.setattr(distro, 'id', lambda: 'ubuntu')
    monkeypatch.setattr(distro, 'lsb_release_info', lambda: {'codename': None})
    monkeypatch.setattr(distro, 'codename', lambda: '')

    assert get_distribution_codename() is None

def test_get_distribution_codename_linux_version_codename(mock_platform_linux, monkeypatch):
    mock_os_release_info = {
        'version_codename': 'focal'
    }
    monkeypatch.setattr(distro, 'os_release_info', lambda: mock_os_release_info)

    assert get_distribution_codename() == 'focal'

def test_get_distribution_codename_linux_ubuntu_codename(mock_platform_linux, monkeypatch):
    mock_os_release_info = {
        'version_codename': None,
        'ubuntu_codename': 'bionic'
    }
    monkeypatch.setattr(distro, 'os_release_info', lambda: mock_os_release_info)

    assert get_distribution_codename() == 'bionic'

def test_get_distribution_codename_linux_lsb_release_codename(mock_platform_linux, monkeypatch):
    mock_os_release_info = {
        'version_codename': None,
        'ubuntu_codename': None
    }
    monkeypatch.setattr(distro, 'os_release_info', lambda: mock_os_release_info)
    monkeypatch.setattr(distro, 'id', lambda: 'ubuntu')
    monkeypatch.setattr(distro, 'lsb_release_info', lambda: {'codename': 'xenial'})

    assert get_distribution_codename() == 'xenial'

def test_get_distribution_codename_linux_distro_codename(mock_platform_linux, monkeypatch):
    mock_os_release_info = {
        'version_codename': None,
        'ubuntu_codename': None
    }
    monkeypatch.setattr(distro, 'os_release_info', lambda: mock_os_release_info)
    monkeypatch.setattr(distro, 'codename', lambda: 'stretch')

    assert get_distribution_codename() == 'stretch'
