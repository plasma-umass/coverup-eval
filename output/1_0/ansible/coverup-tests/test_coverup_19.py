# file lib/ansible/playbook/loop_control.py:26-40
# lines [26, 28, 29, 30, 31, 32, 34, 35, 37, 38, 39, 40]
# branches []

import pytest
from ansible.playbook.loop_control import LoopControl

# Test function to improve coverage for LoopControl.load
def test_loop_control_load(mocker):
    # Mock the load_data method to verify it's being called correctly
    mocker.patch.object(LoopControl, 'load_data', return_value='mocked_load_data')

    # Create a data dictionary to pass to the load method
    data = {
        '_loop_var': 'my_item',
        '_index_var': 'my_index',
        '_label': 'my_label',
        '_pause': 1.5,
        '_extended': True
    }

    # Call the static load method with the data
    result = LoopControl.load(data)

    # Verify that the load_data method was called with the correct parameters
    LoopControl.load_data.assert_called_once_with(data, variable_manager=None, loader=None)

    # Verify that the result of the load method is as expected
    assert result == 'mocked_load_data', "The result of LoopControl.load should be the return value of load_data"

    # Clean up by unpatching the load_data method
    mocker.stopall()
