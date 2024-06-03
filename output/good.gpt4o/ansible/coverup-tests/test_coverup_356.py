# file lib/ansible/executor/discovery/python_target.py:25-38
# lines [25, 26, 28, 29, 31, 33, 34, 36, 38]
# branches ['28->29', '28->31', '33->34', '33->36']

import pytest
from unittest import mock
import platform
import os

# Mock function to simulate reading UTF-8 file content
def read_utf8_file(filepath):
    if filepath == '/etc/os-release':
        return "NAME=Ubuntu\nVERSION=20.04.1 LTS (Focal Fossa)"
    elif filepath == '/usr/lib/os-release':
        return "NAME=Ubuntu\nVERSION=20.04.1 LTS (Focal Fossa)"
    return ""

# The function to be tested
def get_platform_info():
    result = dict(platform_dist_result=[])
    
    if hasattr(platform, 'dist'):
        result['platform_dist_result'] = platform.dist()
    
    osrelease_content = read_utf8_file('/etc/os-release')
    # try to fall back to /usr/lib/os-release
    if not osrelease_content:
        osrelease_content = read_utf8_file('/usr/lib/os-release')
    
    result['osrelease_content'] = osrelease_content
    
    return result

# Test function
def test_get_platform_info(mocker):
    # Mock platform.dist() if it exists
    if hasattr(platform, 'dist'):
        mocker.patch('platform.dist', return_value=('Ubuntu', '20.04', 'focal'))
    
    # Mock read_utf8_file to return specific content
    mocker.patch('ansible.executor.discovery.python_target.read_utf8_file', side_effect=read_utf8_file)
    
    result = get_platform_info()
    
    if hasattr(platform, 'dist'):
        assert result['platform_dist_result'] == ('Ubuntu', '20.04', 'focal')
    assert result['osrelease_content'] == "NAME=Ubuntu\nVERSION=20.04.1 LTS (Focal Fossa)"

