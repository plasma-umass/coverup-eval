# file: lib/ansible/modules/iptables.py:714-717
# asked: {"lines": [715, 716, 717], "branches": []}
# gained: {"lines": [715, 716, 717], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming the function get_iptables_version is imported from the module
from ansible.modules.iptables import get_iptables_version

def test_get_iptables_version(monkeypatch):
    # Mock the module and its run_command method
    mock_module = Mock()
    mock_module.run_command = Mock(return_value=(0, 'iptables v1.8.4\n', ''))

    # Define the iptables_path
    iptables_path = '/sbin/iptables'

    # Call the function
    version = get_iptables_version(iptables_path, mock_module)

    # Assertions to verify the correct behavior
    assert version == '1.8.4'

    # Ensure run_command was called with the correct parameters
    mock_module.run_command.assert_called_once_with([iptables_path, '--version'], check_rc=True)
