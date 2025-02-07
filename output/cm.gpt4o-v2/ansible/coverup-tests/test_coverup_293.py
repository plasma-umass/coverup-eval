# file: lib/ansible/executor/interpreter_discovery.py:165-178
# asked: {"lines": [165, 166, 168, 169, 171, 173, 174, 176, 178], "branches": [[168, 169], [168, 171], [173, 174], [173, 176]]}
# gained: {"lines": [165, 166, 168, 169, 171, 173, 174, 176, 178], "branches": [[168, 169], [168, 171], [173, 174], [173, 176]]}

import pytest
from ansible.executor.interpreter_discovery import _get_linux_distro
from ansible.module_utils.distro import LinuxDistribution

def test_get_linux_distro_with_dist_result():
    platform_info = {
        'platform_dist_result': ['Ubuntu', '20.04', 'focal']
    }
    distro, version = _get_linux_distro(platform_info)
    assert distro == 'Ubuntu'
    assert version == '20.04'

def test_get_linux_distro_without_osrelease_content():
    platform_info = {
        'platform_dist_result': []
    }
    distro, version = _get_linux_distro(platform_info)
    assert distro == ''
    assert version == ''

def test_get_linux_distro_with_osrelease_content(mocker):
    osrelease_content = "NAME=Ubuntu\nVERSION=20.04.1 LTS (Focal Fossa)\nID=ubuntu\nID_LIKE=debian\nPRETTY_NAME=Ubuntu 20.04.1 LTS\nVERSION_ID=20.04"
    platform_info = {
        'platform_dist_result': [],
        'osrelease_content': osrelease_content
    }
    mocker.patch.object(LinuxDistribution, '_parse_os_release_content', return_value={
        'id': 'ubuntu',
        'version_id': '20.04'
    })
    distro, version = _get_linux_distro(platform_info)
    assert distro == 'ubuntu'
    assert version == '20.04'
