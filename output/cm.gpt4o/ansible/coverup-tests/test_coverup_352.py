# file lib/ansible/cli/arguments/option_helpers.py:90-100
# lines [90, 92, 93, 94, 96, 97, 99, 100]
# branches ['93->94', '93->96', '96->97', '96->99']

import pytest
from unittest import mock
import os
from ansible.cli.arguments.option_helpers import unfrack_path

def test_unfrack_path_with_pathsep(mocker):
    mock_unfrackpath = mocker.patch('ansible.cli.arguments.option_helpers.unfrackpath', side_effect=lambda x: f"unfracked_{x}")
    pathsep = True
    value = f"test{os.pathsep}path{os.pathsep}value"
    expected_result = [f"unfracked_test", f"unfracked_path", f"unfracked_value"]

    result = unfrack_path(pathsep)(value)
    
    assert result == expected_result
    mock_unfrackpath.assert_has_calls([mock.call('test'), mock.call('path'), mock.call('value')])

def test_unfrack_path_with_dash():
    pathsep = False
    value = '-'
    result = unfrack_path(pathsep)(value)
    
    assert result == '-'

def test_unfrack_path_without_pathsep(mocker):
    mock_unfrackpath = mocker.patch('ansible.cli.arguments.option_helpers.unfrackpath', side_effect=lambda x: f"unfracked_{x}")
    pathsep = False
    value = "testpath"
    expected_result = "unfracked_testpath"

    result = unfrack_path(pathsep)(value)
    
    assert result == expected_result
    mock_unfrackpath.assert_called_once_with('testpath')
