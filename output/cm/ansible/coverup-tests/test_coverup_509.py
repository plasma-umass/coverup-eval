# file lib/ansible/modules/apt_repository.py:506-513
# lines [506, 507, 508, 510, 511, 513]
# branches ['510->511', '510->513']

import pytest
from ansible.modules.apt_repository import get_add_ppa_signing_key_callback
from unittest.mock import MagicMock

def test_get_add_ppa_signing_key_callback():
    # Create a mock module with check_mode and run_command attributes
    mock_module = MagicMock()
    mock_module.check_mode = False
    mock_module.run_command = MagicMock()

    # Get the callback function
    callback = get_add_ppa_signing_key_callback(mock_module)
    
    # Ensure that the callback is not None
    assert callback is not None

    # Define a command to be run
    test_command = ['echo', 'test']

    # Run the command using the callback
    callback(test_command)

    # Assert that run_command was called with the correct parameters
    mock_module.run_command.assert_called_once_with(test_command, check_rc=True)

def test_get_add_ppa_signing_key_callback_check_mode():
    # Create a mock module with check_mode and run_command attributes
    mock_module = MagicMock()
    mock_module.check_mode = True
    mock_module.run_command = MagicMock()

    # Get the callback function
    callback = get_add_ppa_signing_key_callback(mock_module)
    
    # Ensure that the callback is None
    assert callback is None

    # Define a command to be run
    test_command = ['echo', 'test']

    # Attempt to run the command using the callback, if it's not None
    if callback:
        callback(test_command)

    # Assert that run_command was not called since we are in check_mode
    mock_module.run_command.assert_not_called()
