# file: lib/ansible/executor/discovery/python_target.py:41-44
# asked: {"lines": [41, 42, 44], "branches": []}
# gained: {"lines": [41, 42, 44], "branches": []}

import pytest
import json
from unittest.mock import patch

# Assuming get_platform_info is a function in the same module
from ansible.executor.discovery.python_target import main, get_platform_info

def test_main(monkeypatch):
    # Mock the get_platform_info function
    mock_info = {"platform": "test_platform", "version": "1.0"}
    
    def mock_get_platform_info():
        return mock_info
    
    monkeypatch.setattr('ansible.executor.discovery.python_target.get_platform_info', mock_get_platform_info)
    
    with patch('builtins.print') as mock_print:
        main()
        mock_print.assert_called_once_with(json.dumps(mock_info))
