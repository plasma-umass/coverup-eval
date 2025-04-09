# file lib/ansible/modules/apt_repository.py:506-513
# lines [506, 507, 508, 510, 511, 513]
# branches ['510->511', '510->513']

import pytest
from unittest.mock import Mock

def test_get_add_ppa_signing_key_callback(mocker):
    # Mock the module and its methods
    module = Mock()
    module.check_mode = False
    module.run_command = Mock()

    # Import the function to be tested
    from ansible.modules.apt_repository import get_add_ppa_signing_key_callback

    # Get the callback function
    callback = get_add_ppa_signing_key_callback(module)

    # Ensure the callback is not None
    assert callback is not None

    # Run the callback with a test command
    test_command = ['echo', 'test']
    callback(test_command)

    # Verify that run_command was called with the correct parameters
    module.run_command.assert_called_once_with(test_command, check_rc=True)

    # Test the check_mode branch
    module.check_mode = True
    callback = get_add_ppa_signing_key_callback(module)

    # Ensure the callback is None in check_mode
    assert callback is None
