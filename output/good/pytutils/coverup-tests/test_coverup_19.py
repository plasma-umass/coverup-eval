# file pytutils/env.py:44-67
# lines [44, 55, 57, 59, 60, 62, 64, 65, 67]
# branches ['59->60', '59->67', '64->59', '64->65']

import os
import pytest
import collections
from pytutils.env import load_env_file

def test_load_env_file_with_mock(mocker):
    # Mock the os.environ to ensure we do not modify the real environment variables
    mock_environ = mocker.patch.dict(os.environ, {}, clear=True)
    
    # Define the lines to be loaded into the environment
    lines = [
        'TEST_VAR=VALUE',
        'ANOTHER_VAR=${TEST_VAR}/subdir',
        'HOMELESS_VAR=$UNDEFINED_VAR/path'
    ]
    
    # Call the function with the mocked environment
    result = load_env_file(lines, write_environ=mock_environ)
    
    # Check the result is as expected
    expected_result = collections.OrderedDict([
        ('TEST_VAR', 'VALUE'),
        ('ANOTHER_VAR', 'VALUE/subdir'),
        ('HOMELESS_VAR', '$UNDEFINED_VAR/path')
    ])
    assert result == expected_result
    
    # Check that the environment was updated correctly
    assert mock_environ['TEST_VAR'] == 'VALUE'
    assert mock_environ['ANOTHER_VAR'] == 'VALUE/subdir'
    assert mock_environ['HOMELESS_VAR'] == '$UNDEFINED_VAR/path'
    
    # Cleanup is handled by the mocker fixture, which will restore os.environ after the test
