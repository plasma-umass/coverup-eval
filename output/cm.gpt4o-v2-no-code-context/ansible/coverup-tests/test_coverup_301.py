# file: lib/ansible/cli/arguments/option_helpers.py:90-100
# asked: {"lines": [90, 92, 93, 94, 96, 97, 99, 100], "branches": [[93, 94], [93, 96], [96, 97], [96, 99]]}
# gained: {"lines": [90, 92, 93, 94, 96, 97, 99, 100], "branches": [[93, 94], [93, 96], [96, 97], [96, 99]]}

import pytest
import os
from ansible.cli.arguments.option_helpers import unfrack_path

@pytest.fixture
def mock_unfrackpath(mocker):
    return mocker.patch('ansible.cli.arguments.option_helpers.unfrackpath', side_effect=lambda x: f"unfracked_{x}")

def test_unfrack_path_with_pathsep(mock_unfrackpath):
    pathsep = True
    test_value = f"test{os.pathsep}value"
    expected_result = [f"unfracked_test", f"unfracked_value"]
    
    inner_function = unfrack_path(pathsep)
    result = inner_function(test_value)
    
    assert result == expected_result

def test_unfrack_path_with_dash(mock_unfrackpath):
    pathsep = False
    test_value = "-"
    expected_result = "-"
    
    inner_function = unfrack_path(pathsep)
    result = inner_function(test_value)
    
    assert result == expected_result

def test_unfrack_path_without_pathsep(mock_unfrackpath):
    pathsep = False
    test_value = "test"
    expected_result = "unfracked_test"
    
    inner_function = unfrack_path(pathsep)
    result = inner_function(test_value)
    
    assert result == expected_result
