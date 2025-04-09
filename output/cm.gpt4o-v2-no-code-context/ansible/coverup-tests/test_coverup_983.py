# file: lib/ansible/executor/discovery/python_target.py:25-38
# asked: {"lines": [26, 28, 29, 31, 33, 34, 36, 38], "branches": [[28, 29], [28, 31], [33, 34], [33, 36]]}
# gained: {"lines": [26, 28, 29, 31, 33, 34, 36, 38], "branches": [[28, 29], [28, 31], [33, 34], [33, 36]]}

import pytest
import platform
from unittest.mock import patch, mock_open

# Assuming the function get_platform_info is imported from the module
from ansible.executor.discovery.python_target import get_platform_info

def test_get_platform_info_with_platform_dist(monkeypatch):
    # Mock platform.dist() to return a specific value
    mock_dist = ('Ubuntu', '20.04', 'focal')
    monkeypatch.setattr(platform, 'dist', lambda: mock_dist, raising=False)
    
    # Mock read_utf8_file to return a specific value
    mock_os_release_content = "NAME=Ubuntu\nVERSION=20.04 LTS (Focal Fossa)"
    with patch('ansible.executor.discovery.python_target.read_utf8_file', return_value=mock_os_release_content):
        result = get_platform_info()
    
    assert result['platform_dist_result'] == mock_dist
    assert result['osrelease_content'] == mock_os_release_content

def test_get_platform_info_without_platform_dist(monkeypatch):
    # Remove platform.dist attribute
    monkeypatch.delattr(platform, 'dist', raising=False)
    
    # Mock read_utf8_file to return a specific value
    mock_os_release_content = "NAME=Ubuntu\nVERSION=20.04 LTS (Focal Fossa)"
    with patch('ansible.executor.discovery.python_target.read_utf8_file', return_value=mock_os_release_content):
        result = get_platform_info()
    
    assert result['platform_dist_result'] == []
    assert result['osrelease_content'] == mock_os_release_content

def test_get_platform_info_fallback_os_release(monkeypatch):
    # Remove platform.dist attribute
    monkeypatch.delattr(platform, 'dist', raising=False)
    
    # Mock read_utf8_file to return None for /etc/os-release and a specific value for /usr/lib/os-release
    mock_os_release_content = "NAME=Ubuntu\nVERSION=20.04 LTS (Focal Fossa)"
    with patch('ansible.executor.discovery.python_target.read_utf8_file', side_effect=[None, mock_os_release_content]):
        result = get_platform_info()
    
    assert result['platform_dist_result'] == []
    assert result['osrelease_content'] == mock_os_release_content
