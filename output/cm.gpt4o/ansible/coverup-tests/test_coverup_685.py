# file lib/ansible/executor/discovery/python_target.py:41-44
# lines [41, 42, 44]
# branches []

import pytest
import json
from unittest.mock import patch

# Assuming the function get_platform_info is defined in the same module
from ansible.executor.discovery.python_target import main

def test_main(mocker):
    # Mock the get_platform_info function
    mock_info = {"platform": "test_platform", "version": "1.0"}
    mock_get_platform_info = mocker.patch('ansible.executor.discovery.python_target.get_platform_info', return_value=mock_info)
    
    # Capture the output of the print statement
    with patch('builtins.print') as mock_print:
        main()
        mock_print.assert_called_once_with(json.dumps(mock_info))
    
    # Ensure the mock was called
    mock_get_platform_info.assert_called_once()
