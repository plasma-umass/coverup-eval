# file lib/ansible/module_utils/facts/network/generic_bsd.py:36-64
# lines [57]
# branches ['56->57']

import pytest
from unittest.mock import MagicMock

# Assuming the GenericBsdIfconfigNetwork class is part of a module named generic_bsd
from ansible.module_utils.facts.network import generic_bsd

@pytest.fixture
def mock_module(mocker):
    mock = MagicMock()
    mock.get_bin_path.side_effect = lambda x: '/usr/bin/' + x
    return mock

def test_populate_executes_line_57(mock_module):
    network = generic_bsd.GenericBsdIfconfigNetwork(mock_module)
    network.get_default_interfaces = MagicMock(return_value=({}, {}))
    network.get_interfaces_info = MagicMock(return_value=({'eth0': {'type': 'ether'}}, {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}))
    network.detect_type_media = MagicMock(return_value={'eth0': {'type': 'ether'}})
    network.merge_default_interface = MagicMock()

    network_facts = network.populate()

    assert 'eth0' in network_facts
    assert network_facts['eth0'] == {'type': 'ether'}
    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['default_ipv4'] == {}
    assert network_facts['default_ipv6'] == {}
    assert network_facts['all_ipv4_addresses'] == []
    assert network_facts['all_ipv6_addresses'] == []

    # Cleanup is not necessary as we are using mocks and not modifying any global state
