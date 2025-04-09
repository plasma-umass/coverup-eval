# file lib/ansible/executor/discovery/python_target.py:25-38
# lines [26, 28, 29, 31, 33, 34, 36, 38]
# branches ['28->29', '28->31', '33->34', '33->36']

import os
import pytest
from ansible.executor.discovery.python_target import get_platform_info

@pytest.fixture
def mock_platform(mocker):
    mocker.patch('ansible.executor.discovery.python_target.platform.system', return_value='Linux')
    mocker.patch('ansible.executor.discovery.python_target.platform.release', return_value='4.15.0-54-generic')
    mocker.patch('ansible.executor.discovery.python_target.platform.version', return_value='#58-Ubuntu SMP Mon Jun 24 10:55:24 UTC 2019')
    mocker.patch('ansible.executor.discovery.python_target.platform.machine', return_value='x86_64')
    mocker.patch('ansible.executor.discovery.python_target.platform.processor', return_value='x86_64')

@pytest.fixture
def mock_read_utf8_file(mocker):
    def read_file_side_effect(path):
        if path == '/etc/os-release':
            return ''
        elif path == '/usr/lib/os-release':
            return 'NAME="Ubuntu"'
        else:
            return None
    mocker.patch('ansible.executor.discovery.python_target.read_utf8_file', side_effect=read_file_side_effect)

def test_get_platform_info_with_fallback_os_release(mock_platform, mock_read_utf8_file):
    result = get_platform_info()
    assert result['platform_dist_result'] == []
    assert result['osrelease_content'] == 'NAME="Ubuntu"'
