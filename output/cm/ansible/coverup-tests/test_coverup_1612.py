# file lib/ansible/cli/arguments/option_helpers.py:90-100
# lines [93, 94, 96, 97, 99]
# branches ['93->94', '93->96', '96->97', '96->99']

import os
import pytest
from ansible.cli.arguments.option_helpers import unfrack_path

# Mock the unfrackpath function to control its behavior for the test
@pytest.fixture
def mock_unfrackpath(mocker):
    return mocker.patch('ansible.cli.arguments.option_helpers.unfrackpath', side_effect=lambda x: x)

# Test function to cover lines 93-99
def test_unfrack_path_with_pathsep(mock_unfrackpath):
    # Create a test value with path separator
    test_value = f"test{os.pathsep}path{os.pathsep}value"
    # Create the inner function with pathsep=True
    inner = unfrack_path(pathsep=True)
    # Call the inner function with the test value
    result = inner(test_value)
    # Assert that the unfrackpath function was called correctly
    assert mock_unfrackpath.call_count == 3
    assert mock_unfrackpath.call_args_list[0][0][0] == 'test'
    assert mock_unfrackpath.call_args_list[1][0][0] == 'path'
    assert mock_unfrackpath.call_args_list[2][0][0] == 'value'
    # Assert that the result is as expected
    assert result == ['test', 'path', 'value']

def test_unfrack_path_with_dash(mock_unfrackpath):
    # Create the inner function with pathsep=False
    inner = unfrack_path(pathsep=False)
    # Call the inner function with the value '-'
    result = inner('-')
    # Assert that the unfrackpath function was not called
    mock_unfrackpath.assert_not_called()
    # Assert that the result is the same as the input value
    assert result == '-'

def test_unfrack_path_without_pathsep(mock_unfrackpath):
    # Create a test value without path separator
    test_value = "testpathvalue"
    # Create the inner function with pathsep=False
    inner = unfrack_path(pathsep=False)
    # Call the inner function with the test value
    result = inner(test_value)
    # Assert that the unfrackpath function was called once with the correct argument
    mock_unfrackpath.assert_called_once_with(test_value)
    # Assert that the result is as expected
    assert result == test_value
