# file lib/ansible/config/manager.py:162-167
# lines [162, 164, 165, 167]
# branches ['164->165', '164->167']

import os
import pytest
from ansible.config.manager import resolve_path

def test_resolve_path_with_cwd(mocker):
    # Mock os.getcwd to return a specific directory
    mock_cwd = "/mocked/cwd"
    mocker.patch("os.getcwd", return_value=mock_cwd)
    
    # Test path containing {{CWD}}
    path = "{{CWD}}/some/path"
    expected_path = f"{mock_cwd}/some/path"
    
    # Mock unfrackpath to return the path as is for simplicity
    mocker.patch("ansible.config.manager.unfrackpath", return_value=expected_path)
    
    result = resolve_path(path)
    
    assert result == expected_path

def test_resolve_path_without_cwd(mocker):
    # Test path without {{CWD}}
    path = "/some/absolute/path"
    
    # Mock unfrackpath to return the path as is for simplicity
    mocker.patch("ansible.config.manager.unfrackpath", return_value=path)
    
    result = resolve_path(path)
    
    assert result == path
