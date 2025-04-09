# file: lib/ansible/module_utils/facts/other/facter.py:46-50
# asked: {"lines": [46, 49, 50], "branches": []}
# gained: {"lines": [46, 49, 50], "branches": []}

import pytest
from ansible.module_utils.facts.other.facter import FacterFactCollector
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock(spec=AnsibleModule)
    return module

def test_run_facter_success(mock_module, mocker):
    facter_path = "/usr/bin/facter"
    expected_rc = 0
    expected_out = '{"fact": "value"}'
    expected_err = ""

    mock_module.run_command.return_value = (expected_rc, expected_out, expected_err)

    collector = FacterFactCollector()
    rc, out, err = collector.run_facter(mock_module, facter_path)

    assert rc == expected_rc
    assert out == expected_out
    assert err == expected_err
    mock_module.run_command.assert_called_once_with(f"{facter_path} --puppet --json")

def test_run_facter_failure(mock_module, mocker):
    facter_path = "/usr/bin/facter"
    expected_rc = 1
    expected_out = ""
    expected_err = "error message"

    mock_module.run_command.return_value = (expected_rc, expected_out, expected_err)

    collector = FacterFactCollector()
    rc, out, err = collector.run_facter(mock_module, facter_path)

    assert rc == expected_rc
    assert out == expected_out
    assert err == expected_err
    mock_module.run_command.assert_called_once_with(f"{facter_path} --puppet --json")
