# file lib/ansible/modules/iptables.py:714-717
# lines [714, 715, 716, 717]
# branches []

import pytest
from unittest.mock import Mock

def test_get_iptables_version(mocker):
    from ansible.modules.iptables import get_iptables_version

    # Mock the module and its run_command method
    module = Mock()
    iptables_path = '/sbin/iptables'
    expected_version = '1.8.4'
    module.run_command.return_value = (0, f'iptables v{expected_version}\n', '')

    # Call the function
    version = get_iptables_version(iptables_path, module)

    # Assertions to verify the postconditions
    assert version == expected_version
    module.run_command.assert_called_once_with([iptables_path, '--version'], check_rc=True)
