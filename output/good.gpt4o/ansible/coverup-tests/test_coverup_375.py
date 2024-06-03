# file lib/ansible/modules/ping.py:71-86
# lines [71, 72, 73, 74, 76, 79, 80, 82, 83, 86]
# branches ['79->80', '79->82']

import pytest
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.ping import main

def test_ping_module(mocker):
    mock_ansible_module = mocker.patch('ansible.modules.ping.AnsibleModule', autospec=True)
    mock_module_instance = mock_ansible_module.return_value
    mock_module_instance.params = {'data': 'pong'}
    mock_module_instance.exit_json = mocker.Mock()

    main()

    mock_module_instance.exit_json.assert_called_once_with(ping='pong')

def test_ping_module_crash(mocker):
    mock_ansible_module = mocker.patch('ansible.modules.ping.AnsibleModule', autospec=True)
    mock_module_instance = mock_ansible_module.return_value
    mock_module_instance.params = {'data': 'crash'}

    with pytest.raises(Exception, match="boom"):
        main()
