# file: lib/ansible/modules/rpm_key.py:239-250
# asked: {"lines": [239, 240, 241, 242, 243, 244, 245, 247, 250], "branches": []}
# gained: {"lines": [239, 240, 241, 242, 243, 244, 245, 247, 250], "branches": []}

import pytest
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.rpm_key import main as rpm_key_main
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_ansible_module(mocker):
    mock_module = mocker.patch('ansible.modules.rpm_key.AnsibleModule', autospec=True)
    return mock_module

@pytest.fixture
def mock_rpm_key(mocker):
    mock_rpm_key = mocker.patch('ansible.modules.rpm_key.RpmKey', autospec=True)
    return mock_rpm_key

def test_main_present_state(mock_ansible_module, mock_rpm_key):
    mock_ansible_module.return_value.params = {
        'state': 'present',
        'key': 'some_key',
        'fingerprint': None,
        'validate_certs': True
    }
    rpm_key_main()
    mock_ansible_module.assert_called_once()
    assert mock_ansible_module.call_args[1]['argument_spec']['state']['default'] == 'present'
    assert mock_ansible_module.call_args[1]['argument_spec']['state']['choices'] == ['absent', 'present']
    assert mock_ansible_module.call_args[1]['argument_spec']['key']['required'] is True
    assert mock_ansible_module.call_args[1]['argument_spec']['validate_certs']['default'] is True
    assert mock_ansible_module.call_args[1]['supports_check_mode'] is True
    mock_rpm_key.assert_called_once_with(mock_ansible_module.return_value)

def test_main_absent_state(mock_ansible_module, mock_rpm_key):
    mock_ansible_module.return_value.params = {
        'state': 'absent',
        'key': 'some_key',
        'fingerprint': None,
        'validate_certs': True
    }
    rpm_key_main()
    mock_ansible_module.assert_called_once()
    assert mock_ansible_module.call_args[1]['argument_spec']['state']['default'] == 'present'
    assert mock_ansible_module.call_args[1]['argument_spec']['state']['choices'] == ['absent', 'present']
    assert mock_ansible_module.call_args[1]['argument_spec']['key']['required'] is True
    assert mock_ansible_module.call_args[1]['argument_spec']['validate_certs']['default'] is True
    assert mock_ansible_module.call_args[1]['supports_check_mode'] is True
    mock_rpm_key.assert_called_once_with(mock_ansible_module.return_value)
