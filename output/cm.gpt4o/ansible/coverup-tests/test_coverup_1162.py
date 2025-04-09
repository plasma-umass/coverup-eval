# file lib/ansible/modules/pip.py:352-360
# lines [353, 354, 355, 356, 358, 359, 360]
# branches ['355->356', '355->358']

import pytest
from unittest.mock import Mock

def test_get_cmd_options(mocker):
    # Mock the module and its run_command method
    module = Mock()
    cmd = "pip install"

    # Mock the run_command to simulate the --help command failing
    module.run_command.return_value = (1, "", "error message")

    # Import the function to be tested
    from ansible.modules.pip import _get_cmd_options

    # Mock the fail_json method to raise an exception
    module.fail_json.side_effect = Exception("Could not get output from pip install --help: error message")

    # Verify that the function raises the correct error
    with pytest.raises(Exception) as excinfo:
        _get_cmd_options(module, cmd)
    assert "Could not get output from pip install --help: error message" in str(excinfo.value)

    # Mock the run_command to simulate the --help command succeeding
    module.run_command.return_value = (0, "--option1 --option2", "")

    # Call the function and verify the output
    cmd_options = _get_cmd_options(module, cmd)
    assert cmd_options == ["--option1", "--option2"]

    # Clean up
    mocker.stopall()
