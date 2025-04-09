# file: lib/ansible/modules/iptables.py:672-675
# asked: {"lines": [672, 673, 674, 675], "branches": []}
# gained: {"lines": [672, 673, 674, 675], "branches": []}

import pytest

def test_check_present(mocker):
    from ansible.modules.iptables import check_present, push_arguments

    iptables_path = "/sbin/iptables"
    module = mocker.Mock()
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': None
    }

    # Mock the push_arguments function
    mocker.patch('ansible.modules.iptables.push_arguments', return_value=[iptables_path, '-t', 'filter', '-C', 'INPUT'])

    # Mock the run_command method
    module.run_command = mocker.Mock(return_value=(0, '', ''))

    # Call the function
    result = check_present(iptables_path, module, params)

    # Assertions
    module.run_command.assert_called_once_with([iptables_path, '-t', 'filter', '-C', 'INPUT'], check_rc=False)
    assert result == True

    # Test the case where the command returns a non-zero return code
    module.run_command = mocker.Mock(return_value=(1, '', ''))
    result = check_present(iptables_path, module, params)
    assert result == False
