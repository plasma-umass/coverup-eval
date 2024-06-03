# file lib/ansible/modules/rpm_key.py:239-250
# lines [239, 240, 241, 242, 243, 244, 245, 247, 250]
# branches []

import pytest
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.rpm_key import main as rpm_key_main
from unittest.mock import patch

@pytest.fixture
def mock_ansible_module(mocker):
    mock_module = mocker.patch('ansible.modules.rpm_key.AnsibleModule', autospec=True)
    return mock_module

def test_rpm_key_present(mock_ansible_module):
    mock_ansible_module.return_value.params = {
        'state': 'present',
        'key': 'test-key',
        'fingerprint': None,
        'validate_certs': True
    }
    with patch('ansible.modules.rpm_key.RpmKey') as mock_rpm_key:
        rpm_key_main()
        mock_rpm_key.assert_called_once_with(mock_ansible_module.return_value)

def test_rpm_key_absent(mock_ansible_module):
    mock_ansible_module.return_value.params = {
        'state': 'absent',
        'key': 'test-key',
        'fingerprint': None,
        'validate_certs': True
    }
    with patch('ansible.modules.rpm_key.RpmKey') as mock_rpm_key:
        rpm_key_main()
        mock_rpm_key.assert_called_once_with(mock_ansible_module.return_value)
