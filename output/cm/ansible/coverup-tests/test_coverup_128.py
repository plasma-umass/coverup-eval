# file lib/ansible/module_utils/common/sys_info.py:82-109
# lines [82, 89, 90, 94, 95, 97, 98, 100, 101, 102, 104, 105, 106, 107, 109]
# branches ['90->94', '90->109', '97->98', '97->100', '100->101', '100->104', '104->105', '104->109', '106->107', '106->109']

import pytest
from unittest.mock import patch
from ansible.module_utils.common.sys_info import get_distribution_codename

@pytest.fixture
def mock_distro(monkeypatch):
    mock_distro_module = pytest.importorskip("distro")
    monkeypatch.setattr("ansible.module_utils.common.sys_info.distro", mock_distro_module)
    return mock_distro_module

def test_get_distribution_codename_linux_no_codename(mock_distro, monkeypatch):
    # Mock platform.system to return 'Linux'
    monkeypatch.setattr("platform.system", lambda: "Linux")
    # Mock distro.os_release_info to return a dict without 'version_codename' and 'ubuntu_codename'
    monkeypatch.setattr(mock_distro, "os_release_info", lambda: {'name': 'TestLinux'})
    # Mock distro.id to return 'ubuntu'
    monkeypatch.setattr(mock_distro, "id", lambda: 'ubuntu')
    # Mock distro.lsb_release_info to return a dict without 'codename'
    monkeypatch.setattr(mock_distro, "lsb_release_info", lambda: {'description': 'TestUbuntu'})
    # Mock distro.codename to return an empty string
    monkeypatch.setattr(mock_distro, "codename", lambda: u'')

    codename = get_distribution_codename()
    assert codename is None, "Expected codename to be None when no codename is found"

def test_get_distribution_codename_linux_with_codename(mock_distro, monkeypatch):
    # Mock platform.system to return 'Linux'
    monkeypatch.setattr("platform.system", lambda: "Linux")
    # Mock distro.os_release_info to return a dict with 'version_codename'
    monkeypatch.setattr(mock_distro, "os_release_info", lambda: {'version_codename': 'focal'})
    # Mock distro.id to return 'ubuntu'
    monkeypatch.setattr(mock_distro, "id", lambda: 'ubuntu')
    # Mock distro.lsb_release_info to return a dict with 'codename'
    monkeypatch.setattr(mock_distro, "lsb_release_info", lambda: {'codename': 'focal'})
    # Mock distro.codename to return a non-empty string
    monkeypatch.setattr(mock_distro, "codename", lambda: 'focal')

    codename = get_distribution_codename()
    assert codename == 'focal', "Expected codename to be 'focal'"

def test_get_distribution_codename_non_linux(monkeypatch):
    # Mock platform.system to return 'NonLinux'
    monkeypatch.setattr("platform.system", lambda: "NonLinux")

    codename = get_distribution_codename()
    assert codename is None, "Expected codename to be None when not on a Linux system"
