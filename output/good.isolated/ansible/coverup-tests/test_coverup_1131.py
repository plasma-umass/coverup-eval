# file lib/ansible/modules/getent.py:125-196
# lines [125, 126, 127, 128, 129, 130, 131, 132, 134, 137, 139, 140, 141, 142, 143, 145, 147, 148, 150, 152, 153, 155, 156, 158, 159, 160, 161, 163, 164, 165, 167, 168, 169, 170, 172, 174, 175, 177, 178, 181, 182, 184, 186, 187, 188, 189, 190, 191, 192, 193, 194, 196]
# branches ['147->148', '147->150', '152->153', '152->155', '155->156', '155->158', '167->168', '167->186', '169->170', '169->184', '172->174', '172->181', '174->175', '174->177', '186->187', '186->188', '188->189', '188->193', '190->191', '190->196', '193->194', '193->196']

import pytest
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.getent import main as getent_main
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_module(monkeypatch):
    mock_ansible_module = MagicMock()
    monkeypatch.setattr(AnsibleModule, "fail_json", mock_ansible_module.fail_json)
    monkeypatch.setattr(AnsibleModule, "exit_json", mock_ansible_module.exit_json)
    monkeypatch.setattr(AnsibleModule, "run_command", mock_ansible_module.run_command)
    monkeypatch.setattr(AnsibleModule, "get_bin_path", lambda *args, **kwargs: '/usr/bin/getent')
    return mock_ansible_module

def test_getent_module_fail_key_false(mock_module, monkeypatch):
    mock_module.run_command.return_value = (2, '', '')  # Simulate return code 2 from getent command
    params = {'database': 'passwd', 'key': 'nonexistent', 'fail_key': False}
    monkeypatch.setattr(AnsibleModule, "__init__", lambda self, **kwargs: setattr(self, "params", params))
    getent_main()
    mock_module.exit_json.assert_called_once_with(ansible_facts={'getent_passwd': {'nonexistent': None}}, msg="One or more supplied key could not be found in the database.")

def test_getent_module_fail_key_true(mock_module, monkeypatch):
    mock_module.run_command.return_value = (2, '', '')  # Simulate return code 2 from getent command
    params = {'database': 'passwd', 'key': 'nonexistent', 'fail_key': True}
    monkeypatch.setattr(AnsibleModule, "__init__", lambda self, **kwargs: setattr(self, "params", params))
    getent_main()
    mock_module.fail_json.assert_called_once_with(msg="One or more supplied key could not be found in the database.")
