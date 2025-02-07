# file: lib/ansible/modules/iptables.py:714-717
# asked: {"lines": [714, 715, 716, 717], "branches": []}
# gained: {"lines": [714, 715, 716, 717], "branches": []}

import pytest
from unittest.mock import Mock

def test_get_iptables_version(monkeypatch):
    # Mock the module and its run_command method
    module = Mock()
    module.run_command = Mock(return_value=(0, 'iptables v1.8.4\n', ''))

    # Define the iptables_path
    iptables_path = '/sbin/iptables'

    # Import the function to test
    from ansible.modules.iptables import get_iptables_version

    # Call the function
    version = get_iptables_version(iptables_path, module)

    # Assert the expected version is returned
    assert version == '1.8.4'

    # Ensure run_command was called with the correct parameters
    module.run_command.assert_called_once_with([iptables_path, '--version'], check_rc=True)
