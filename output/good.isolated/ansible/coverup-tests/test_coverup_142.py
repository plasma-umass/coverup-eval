# file lib/ansible/modules/replace.py:192-210
# lines [192, 194, 195, 196, 197, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210]
# branches ['201->202', '201->209', '202->203', '202->204', '206->207', '206->209', '209->exit', '209->210']

import os
import pytest
import tempfile
from unittest.mock import MagicMock

# Assuming the module ansible.modules.replace is available in the PYTHONPATH
from ansible.modules.replace import write_changes

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.tmpdir = tempfile.gettempdir()
    mock_module.params = {
        'validate': None,
        'unsafe_writes': False
    }
    mock_module.fail_json = MagicMock()
    mock_module.atomic_move = MagicMock()
    return mock_module

def test_write_changes_with_validation_failure(mock_module, mocker):
    # Set up the mock module to have a validation command
    mock_module.params['validate'] = "echo 'invalid' && exit 1 %s"
    
    # Mock the run_command method to simulate validation failure
    mocker.patch.object(mock_module, 'run_command', return_value=(1, '', 'Validation error'))

    # Create a temporary file to replace
    _, path = tempfile.mkstemp()
    try:
        # Call the function with the mock module
        write_changes(mock_module, b"content", path)
        
        # Assert that fail_json was called due to validation failure
        assert mock_module.fail_json.called
        assert mock_module.fail_json.call_args[1]['msg'].startswith('failed to validate:')
    finally:
        # Clean up the temporary file
        os.remove(path)

def test_write_changes_with_no_validation(mock_module):
    # Create a temporary file to replace
    _, path = tempfile.mkstemp()
    try:
        # Call the function with the mock module
        write_changes(mock_module, b"content", path)
        
        # Assert that atomic_move was called since there was no validation
        assert mock_module.atomic_move.called
    finally:
        # Clean up the temporary file
        os.remove(path)

def test_write_changes_with_validation_success(mock_module, mocker):
    # Set up the mock module to have a validation command
    mock_module.params['validate'] = "echo 'valid' && exit 0 %s"
    
    # Mock the run_command method to simulate validation success
    mocker.patch.object(mock_module, 'run_command', return_value=(0, '', ''))

    # Create a temporary file to replace
    _, path = tempfile.mkstemp()
    try:
        # Call the function with the mock module
        write_changes(mock_module, b"content", path)
        
        # Assert that atomic_move was called due to successful validation
        assert mock_module.atomic_move.called
    finally:
        # Clean up the temporary file
        os.remove(path)
