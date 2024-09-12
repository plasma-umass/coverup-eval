# file: lib/ansible/executor/discovery/python_target.py:25-38
# asked: {"lines": [29, 34], "branches": [[28, 29], [33, 34]]}
# gained: {"lines": [29, 34], "branches": [[28, 29], [33, 34]]}

import pytest
import platform
from unittest.mock import patch, mock_open

# Assuming the function get_platform_info is defined in a module named python_target
from ansible.executor.discovery.python_target import get_platform_info

@pytest.fixture
def mock_platform_dist(monkeypatch):
    def mock_dist():
        return ('Ubuntu', '20.04', 'focal')
    monkeypatch.setattr(platform, 'dist', mock_dist, raising=False)

@pytest.fixture
def mock_read_utf8_file(monkeypatch):
    def mock_read(path, encoding='utf-8'):
        if path == '/etc/os-release':
            return None
        elif path == '/usr/lib/os-release':
            return 'NAME="Ubuntu"\nVERSION="20.04 LTS (Focal Fossa)"'
        return None
    monkeypatch.setattr('ansible.executor.discovery.python_target.read_utf8_file', mock_read)

def test_get_platform_info_with_platform_dist(mock_platform_dist, mock_read_utf8_file):
    result = get_platform_info()
    assert result['platform_dist_result'] == ('Ubuntu', '20.04', 'focal')
    assert result['osrelease_content'] == 'NAME="Ubuntu"\nVERSION="20.04 LTS (Focal Fossa)"'

def test_get_platform_info_without_platform_dist(mock_read_utf8_file, monkeypatch):
    monkeypatch.delattr(platform, 'dist', raising=False)
    result = get_platform_info()
    assert result['platform_dist_result'] == []
    assert result['osrelease_content'] == 'NAME="Ubuntu"\nVERSION="20.04 LTS (Focal Fossa)"'
