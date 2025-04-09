# file lib/ansible/executor/interpreter_discovery.py:165-178
# lines [166, 168, 169, 171, 173, 174, 176, 178]
# branches ['168->169', '168->171', '173->174', '173->176']

import pytest
from ansible.executor.interpreter_discovery import _get_linux_distro, LinuxDistribution

def test_get_linux_distro_with_platform_dist_result():
    platform_info = {
        'platform_dist_result': ['Ubuntu', '20.04', 'focal']
    }
    distro, version = _get_linux_distro(platform_info)
    assert distro == 'Ubuntu'
    assert version == '20.04'

def test_get_linux_distro_with_empty_platform_dist_result():
    platform_info = {
        'platform_dist_result': []
    }
    distro, version = _get_linux_distro(platform_info)
    assert distro == ''
    assert version == ''

def test_get_linux_distro_with_osrelease_content(mocker):
    osrelease_content = """
    NAME="Ubuntu"
    VERSION="20.04.1 LTS (Focal Fossa)"
    ID=ubuntu
    VERSION_ID="20.04"
    """
    platform_info = {
        'osrelease_content': osrelease_content
    }
    mocker.patch.object(LinuxDistribution, '_parse_os_release_content', return_value={
        'id': 'ubuntu',
        'version_id': '20.04'
    })
    distro, version = _get_linux_distro(platform_info)
    assert distro == 'ubuntu'
    assert version == '20.04'

def test_get_linux_distro_with_empty_osrelease_content():
    platform_info = {
        'osrelease_content': ''
    }
    distro, version = _get_linux_distro(platform_info)
    assert distro == ''
    assert version == ''
