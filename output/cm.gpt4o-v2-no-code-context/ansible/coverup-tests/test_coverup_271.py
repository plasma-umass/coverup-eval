# file: lib/ansible/executor/interpreter_discovery.py:165-178
# asked: {"lines": [165, 166, 168, 169, 171, 173, 174, 176, 178], "branches": [[168, 169], [168, 171], [173, 174], [173, 176]]}
# gained: {"lines": [165, 166, 168, 169, 171, 173, 174, 176, 178], "branches": [[168, 169], [168, 171], [173, 174], [173, 176]]}

import pytest
from ansible.executor.interpreter_discovery import _get_linux_distro, LinuxDistribution

def test_get_linux_distro_with_platform_dist_result(monkeypatch):
    platform_info = {
        'platform_dist_result': ['Ubuntu', '20.04', 'focal']
    }
    result = _get_linux_distro(platform_info)
    assert result == ('Ubuntu', '20.04')

def test_get_linux_distro_with_empty_platform_dist_result(monkeypatch):
    platform_info = {
        'platform_dist_result': []
    }
    result = _get_linux_distro(platform_info)
    assert result == ('', '')

def test_get_linux_distro_with_osrelease_content(monkeypatch):
    osrelease_content = "NAME=Ubuntu\nVERSION_ID=20.04"
    platform_info = {
        'osrelease_content': osrelease_content
    }

    def mock_parse_os_release_content(content):
        return {'id': 'ubuntu', 'version_id': '20.04'}

    monkeypatch.setattr(LinuxDistribution, '_parse_os_release_content', mock_parse_os_release_content)
    result = _get_linux_distro(platform_info)
    assert result == ('ubuntu', '20.04')

def test_get_linux_distro_with_empty_osrelease_content(monkeypatch):
    platform_info = {
        'osrelease_content': ''
    }
    result = _get_linux_distro(platform_info)
    assert result == ('', '')

def test_get_linux_distro_with_no_osrelease_content(monkeypatch):
    platform_info = {}
    result = _get_linux_distro(platform_info)
    assert result == ('', '')
