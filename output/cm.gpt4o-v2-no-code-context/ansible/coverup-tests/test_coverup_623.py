# file: lib/ansible/executor/discovery/python_target.py:41-44
# asked: {"lines": [41, 42, 44], "branches": []}
# gained: {"lines": [41, 42, 44], "branches": []}

import pytest
import json
from ansible.executor.discovery.python_target import main, get_platform_info

def test_main(monkeypatch, capsys):
    # Mock get_platform_info to return a known value
    mock_info = {"platform": "test_platform", "version": "1.0"}
    monkeypatch.setattr('ansible.executor.discovery.python_target.get_platform_info', lambda: mock_info)
    
    # Call the main function
    main()
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Assert that the output is the JSON representation of the mock_info
    assert json.loads(captured.out) == mock_info
