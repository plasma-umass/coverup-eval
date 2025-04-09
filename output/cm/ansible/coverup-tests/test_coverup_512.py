# file lib/ansible/modules/iptables.py:553-556
# lines [553, 554, 555, 556]
# branches ['554->exit', '554->555', '555->exit', '555->556']

import pytest
from ansible.modules.iptables import append_tcp_flags

@pytest.fixture
def iptables_cleanup():
    # Setup code if needed (e.g., to ensure iptables rules are in a known state)
    yield
    # Teardown code to clean up after the test
    # (e.g., remove any iptables rules added by the test)
    # This is just a placeholder as the actual iptables command is not being run

def test_append_tcp_flags_with_flags_and_flags_set(mocker, iptables_cleanup):
    # Mocking the extend method to prevent actual changes to system iptables
    mock_rule = mocker.MagicMock()

    # Define the parameters with both 'flags' and 'flags_set'
    param = {
        'flags': ['SYN', 'ACK'],
        'flags_set': ['RST', 'FIN']
    }
    flag = '--tcp-flags'

    # Call the function with the parameters
    append_tcp_flags(mock_rule, param, flag)

    # Assert that the extend method was called with the correct arguments
    mock_rule.extend.assert_called_once_with([flag, 'SYN,ACK', 'RST,FIN'])

def test_append_tcp_flags_without_flags(mocker, iptables_cleanup):
    # Mocking the extend method to prevent actual changes to system iptables
    mock_rule = mocker.MagicMock()

    # Define the parameters without 'flags' but with 'flags_set'
    param = {
        'flags_set': ['RST', 'FIN']
    }
    flag = '--tcp-flags'

    # Call the function with the parameters
    append_tcp_flags(mock_rule, param, flag)

    # Assert that the extend method was not called since 'flags' is missing
    mock_rule.extend.assert_not_called()

def test_append_tcp_flags_without_flags_set(mocker, iptables_cleanup):
    # Mocking the extend method to prevent actual changes to system iptables
    mock_rule = mocker.MagicMock()

    # Define the parameters with 'flags' but without 'flags_set'
    param = {
        'flags': ['SYN', 'ACK']
    }
    flag = '--tcp-flags'

    # Call the function with the parameters
    append_tcp_flags(mock_rule, param, flag)

    # Assert that the extend method was not called since 'flags_set' is missing
    mock_rule.extend.assert_not_called()
