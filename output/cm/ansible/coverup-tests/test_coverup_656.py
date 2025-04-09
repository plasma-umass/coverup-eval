# file lib/ansible/modules/iptables.py:576-578
# lines [576, 577, 578]
# branches ['577->exit', '577->578']

import pytest
from ansible.modules.iptables import append_jump

@pytest.fixture
def iptables_cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_append_jump_with_param(mocker, iptables_cleanup):
    # Mocking the extend method to verify it's called with correct parameters
    mock_rule = mocker.MagicMock()

    # Call the function with param set to True
    append_jump(mock_rule, True, 'ACCEPT')

    # Assert that extend was called with ['-j', 'ACCEPT']
    mock_rule.extend.assert_called_once_with(['-j', 'ACCEPT'])

def test_append_jump_without_param(mocker, iptables_cleanup):
    # Mocking the extend method to verify it's not called when param is False
    mock_rule = mocker.MagicMock()

    # Call the function with param set to False
    append_jump(mock_rule, False, 'ACCEPT')

    # Assert that extend was not called
    mock_rule.extend.assert_not_called()
