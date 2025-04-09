# file lib/ansible/modules/pip.py:352-360
# lines [352, 353, 354, 355, 356, 358, 359, 360]
# branches ['355->356', '355->358']

import pytest
from unittest.mock import MagicMock

# Assuming the _get_cmd_options function is part of a module named ansible.modules.pip
# and not the actual pip package, we need to adjust the import statement accordingly.

@pytest.fixture
def mock_module(mocker):
    mock = MagicMock()
    mock.run_command.return_value = (0, "--version --help --some-option", "")
    return mock

def test_get_cmd_options_success(mock_module, mocker):
    mocker.patch('ansible.modules.pip.AnsibleModule', return_value=mock_module)
    from ansible.modules.pip import _get_cmd_options

    cmd = "pip"
    expected_options = ["--version", "--help", "--some-option"]
    options = _get_cmd_options(mock_module, cmd)
    
    assert options == expected_options
    mock_module.run_command.assert_called_once_with("pip --help")

def test_get_cmd_options_failure(mock_module, mocker):
    mocker.patch('ansible.modules.pip.AnsibleModule', return_value=mock_module)
    from ansible.modules.pip import _get_cmd_options

    mock_module.run_command.return_value = (1, "", "Error message")
    cmd = "pip"

    # The original test expected an Exception to be raised, but the actual code
    # calls fail_json on the module, which does not raise an Exception.
    # Instead, we should check that fail_json was called with the correct message.
    _get_cmd_options(mock_module, cmd)
    
    mock_module.fail_json.assert_called_once_with(msg="Could not get output from pip --help: Error message")
