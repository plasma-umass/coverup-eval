# file: lib/ansible/executor/interpreter_discovery.py:165-178
# asked: {"lines": [165, 166, 168, 169, 171, 173, 174, 176, 178], "branches": [[168, 169], [168, 171], [173, 174], [173, 176]]}
# gained: {"lines": [165, 166, 168, 169, 171, 173, 174, 176, 178], "branches": [[168, 169], [168, 171], [173, 174], [173, 176]]}

import pytest
from ansible.executor.interpreter_discovery import _get_linux_distro
from ansible.module_utils.distro import LinuxDistribution

@pytest.fixture
def mock_linux_distribution(mocker):
    mocker.patch.object(LinuxDistribution, '_parse_os_release_content', return_value={'id': 'test_id', 'version_id': 'test_version'})

def test_get_linux_distro_with_platform_dist_result():
    platform_info = {
        'platform_dist_result': ['test_dist', 'test_version', 'extra']
    }
    result = _get_linux_distro(platform_info)
    assert result == ('test_dist', 'test_version')

def test_get_linux_distro_with_empty_osrelease_content():
    platform_info = {
        'platform_dist_result': []
    }
    result = _get_linux_distro(platform_info)
    assert result == ('', '')

def test_get_linux_distro_with_osrelease_content(mock_linux_distribution):
    platform_info = {
        'platform_dist_result': [],
        'osrelease_content': 'NAME="TestOS"\nVERSION="1.0"\nID=test_id\nVERSION_ID=test_version\n'
    }
    result = _get_linux_distro(platform_info)
    assert result == ('test_id', 'test_version')
