# file lib/ansible/plugins/callback/junit.py:133-154
# lines [133, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 149, 151, 153, 154]
# branches ['153->exit', '153->154']

import os
import pytest
from unittest.mock import patch
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def cleanup_output_dir():
    # Setup code
    output_dir = os.path.expanduser('~/.ansible.log')
    yield output_dir
    # Teardown code
    if os.path.exists(output_dir):
        os.rmdir(output_dir)

def test_callback_module_init_creates_output_dir_if_not_exists(mocker, cleanup_output_dir):
    output_dir = cleanup_output_dir
    # Ensure the directory does not exist before the test
    if os.path.exists(output_dir):
        os.rmdir(output_dir)
    
    with patch('os.makedirs') as mock_makedirs:
        # Instantiate the CallbackModule, which should create the output directory
        CallbackModule()
        
        # Assert that os.makedirs was called with the correct output directory
        mock_makedirs.assert_called_once_with(output_dir)
        
        # The directory existence check is removed because we are mocking os.makedirs
        # and the actual directory will not be created in the file system.
