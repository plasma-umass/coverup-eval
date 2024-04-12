# file lib/ansible/modules/iptables.py:693-695
# lines [693, 694, 695]
# branches []

import pytest
from ansible.modules.iptables import flush_table
from unittest.mock import MagicMock

@pytest.fixture
def iptables_cleanup():
    # Setup code to ensure a clean environment before running the test
    # This could involve backing up current iptables rules, for example
    # However, for the purpose of this example, we'll assume it's a mock environment
    yield
    # Teardown code to clean up after the test
    # This would restore the original iptables rules, for example
    # Again, we'll assume it's a mock and no actual cleanup is needed

def test_flush_table(mocker, iptables_cleanup):
    # Mock the module and params
    module_mock = MagicMock()
    params_mock = {"table": "filter"}

    # Mock the run_command method to assert it is called with the correct arguments
    module_mock.run_command = MagicMock(return_value=(0, "", ""))

    # Mock the iptables_path
    iptables_path = "/sbin/iptables"

    # Use pytest-mock to mock the push_arguments function
    push_arguments_mock = mocker.patch('ansible.modules.iptables.push_arguments')
    push_arguments_mock.return_value = [iptables_path, '-F']

    # Call the function to test
    flush_table(iptables_path, module_mock, params_mock)

    # Assert that push_arguments was called with the correct arguments
    push_arguments_mock.assert_called_once_with(iptables_path, '-F', params_mock, make_rule=False)

    # Assert that run_command was called with the correct arguments
    module_mock.run_command.assert_called_once_with([iptables_path, '-F'], check_rc=True)
