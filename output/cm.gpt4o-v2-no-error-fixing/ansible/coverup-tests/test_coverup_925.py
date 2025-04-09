# file: lib/ansible/module_utils/facts/network/generic_bsd.py:36-64
# asked: {"lines": [57], "branches": [[56, 57]]}
# gained: {"lines": [57], "branches": [[56, 57]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.side_effect = lambda x: f"/sbin/{x}" if x in ["ifconfig", "route"] else None
    return module

@pytest.fixture
def network_instance(mock_module):
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    return GenericBsdIfconfigNetwork(mock_module)

def test_populate_all_branches(network_instance, mock_module):
    # Mocking methods to return controlled data
    network_instance.get_default_interfaces = MagicMock(return_value=("em0", "em1"))
    network_instance.get_interfaces_info = MagicMock(return_value=({"em0": {"ipv4": "192.168.1.1"}, "em1": {"ipv6": "fe80::1"}}, {"all_ipv4_addresses": ["192.168.1.1"], "all_ipv6_addresses": ["fe80::1"]}))
    network_instance.detect_type_media = MagicMock(side_effect=lambda x: x)
    network_instance.merge_default_interface = MagicMock()

    # Call the method
    result = network_instance.populate()

    # Assertions to ensure all lines are executed
    assert "interfaces" in result
    assert "em0" in result
    assert "em1" in result
    assert result["em0"] == {"ipv4": "192.168.1.1"}
    assert result["em1"] == {"ipv6": "fe80::1"}
    assert result["default_ipv4"] == "em0"
    assert result["default_ipv6"] == "em1"
    assert result["all_ipv4_addresses"] == ["192.168.1.1"]
    assert result["all_ipv6_addresses"] == ["fe80::1"]

    # Ensure the merge_default_interface was called correctly
    network_instance.merge_default_interface.assert_any_call("em0", {"em0": {"ipv4": "192.168.1.1"}, "em1": {"ipv6": "fe80::1"}}, 'ipv4')
    network_instance.merge_default_interface.assert_any_call("em1", {"em0": {"ipv4": "192.168.1.1"}, "em1": {"ipv6": "fe80::1"}}, 'ipv6')
