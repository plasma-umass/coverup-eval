# file: lib/ansible/executor/discovery/python_target.py:25-38
# asked: {"lines": [25, 26, 28, 29, 31, 33, 34, 36, 38], "branches": [[28, 29], [28, 31], [33, 34], [33, 36]]}
# gained: {"lines": [25, 26, 28, 31, 33, 34, 36, 38], "branches": [[28, 31], [33, 34], [33, 36]]}

import pytest
import platform
from unittest.mock import patch, mock_open

# Assuming the functions are imported from the module
from ansible.executor.discovery.python_target import get_platform_info, read_utf8_file

def test_get_platform_info_with_platform_dist(monkeypatch):
    # Mock platform.dist() if it exists
    if hasattr(platform, 'dist'):
        monkeypatch.setattr(platform, 'dist', lambda: ('Ubuntu', '20.04', 'focal'))
    
    # Mock read_utf8_file to return specific content
    def mock_read_utf8_file(path):
        if path == '/etc/os-release':
            return 'NAME="Ubuntu"\nVERSION="20.04 LTS (Focal Fossa)"'
        return None
    
    monkeypatch.setattr('ansible.executor.discovery.python_target.read_utf8_file', mock_read_utf8_file)
    
    result = get_platform_info()
    
    if hasattr(platform, 'dist'):
        assert result['platform_dist_result'] == ('Ubuntu', '20.04', 'focal')
    assert result['osrelease_content'] == 'NAME="Ubuntu"\nVERSION="20.04 LTS (Focal Fossa)"'

def test_get_platform_info_without_platform_dist(monkeypatch):
    # Ensure platform.dist() does not exist
    if hasattr(platform, 'dist'):
        monkeypatch.delattr(platform, 'dist')
    
    # Mock read_utf8_file to return specific content
    def mock_read_utf8_file(path):
        if path == '/etc/os-release':
            return 'NAME="Ubuntu"\nVERSION="20.04 LTS (Focal Fossa)"'
        return None
    
    monkeypatch.setattr('ansible.executor.discovery.python_target.read_utf8_file', mock_read_utf8_file)
    
    result = get_platform_info()
    
    assert result['platform_dist_result'] == []
    assert result['osrelease_content'] == 'NAME="Ubuntu"\nVERSION="20.04 LTS (Focal Fossa)"'

def test_get_platform_info_fallback_os_release(monkeypatch):
    # Ensure platform.dist() does not exist
    if hasattr(platform, 'dist'):
        monkeypatch.delattr(platform, 'dist')
    
    # Mock read_utf8_file to return None for /etc/os-release and specific content for /usr/lib/os-release
    def mock_read_utf8_file(path):
        if path == '/etc/os-release':
            return None
        if path == '/usr/lib/os-release':
            return 'NAME="Ubuntu"\nVERSION="20.04 LTS (Focal Fossa)"'
        return None
    
    monkeypatch.setattr('ansible.executor.discovery.python_target.read_utf8_file', mock_read_utf8_file)
    
    result = get_platform_info()
    
    assert result['platform_dist_result'] == []
    assert result['osrelease_content'] == 'NAME="Ubuntu"\nVERSION="20.04 LTS (Focal Fossa)"'
