# file lib/ansible/executor/interpreter_discovery.py:165-178
# lines [165, 166, 168, 169, 171, 173, 174, 176, 178]
# branches ['168->169', '168->171', '173->174', '173->176']

import pytest
from ansible.executor.interpreter_discovery import _get_linux_distro

class MockLinuxDistribution:
    @staticmethod
    def _parse_os_release_content(osrelease_content):
        return {
            'id': 'test_id',
            'version_id': 'test_version_id'
        }

@pytest.fixture
def mock_platform_info(mocker):
    return {
        'platform_dist_result': [],
        'osrelease_content': 'NAME="TestOS"\nVERSION="1.0"\nID=test_id\nVERSION_ID=test_version_id'
    }

def test_get_linux_distro_with_empty_platform_dist_result_and_valid_osrelease_content(mock_platform_info, mocker):
    mocker.patch('ansible.executor.interpreter_discovery.LinuxDistribution', MockLinuxDistribution)
    distro_id, distro_version = _get_linux_distro(mock_platform_info)
    assert distro_id == 'test_id'
    assert distro_version == 'test_version_id'

def test_get_linux_distro_with_empty_platform_dist_result_and_no_osrelease_content(mock_platform_info, mocker):
    mock_platform_info['osrelease_content'] = None
    mocker.patch('ansible.executor.interpreter_discovery.LinuxDistribution', MockLinuxDistribution)
    distro_id, distro_version = _get_linux_distro(mock_platform_info)
    assert distro_id == ''
    assert distro_version == ''

def test_get_linux_distro_with_valid_platform_dist_result(mock_platform_info):
    mock_platform_info['platform_dist_result'] = ['test_id', 'test_version_id', '']
    distro_id, distro_version = _get_linux_distro(mock_platform_info)
    assert distro_id == 'test_id'
    assert distro_version == 'test_version_id'

def test_get_linux_distro_with_invalid_platform_dist_result(mock_platform_info):
    mock_platform_info['platform_dist_result'] = ['', '', '']
    distro_id, distro_version = _get_linux_distro(mock_platform_info)
    assert distro_id == 'test_id'
    assert distro_version == 'test_version_id'
