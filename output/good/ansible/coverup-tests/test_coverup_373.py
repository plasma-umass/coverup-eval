# file lib/ansible/modules/ping.py:71-86
# lines [71, 72, 73, 74, 76, 79, 80, 82, 83, 86]
# branches ['79->80', '79->82']

import pytest
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.ping import main as ping_main

def test_ping_module_success(mocker):
    # Mock the AnsibleModule to return 'pong' when 'data' is accessed
    mock_module = mocker.patch('ansible.modules.ping.AnsibleModule')
    mock_module.return_value.params = {'data': 'pong'}
    mock_module.return_value.exit_json = mocker.Mock()

    # Run the main function of the ping module
    ping_main()

    # Assert that exit_json was called with the expected result
    mock_module.return_value.exit_json.assert_called_once_with(ping='pong')

def test_ping_module_crash(mocker):
    # Mock the AnsibleModule to return 'crash' when 'data' is accessed
    mock_module = mocker.patch('ansible.modules.ping.AnsibleModule')
    mock_module.return_value.params = {'data': 'crash'}

    # Assert that running the main function of the ping module raises an Exception
    with pytest.raises(Exception) as exc_info:
        ping_main()
    assert str(exc_info.value) == "boom"
