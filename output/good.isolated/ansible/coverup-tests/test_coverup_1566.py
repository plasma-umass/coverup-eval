# file lib/ansible/module_utils/facts/network/hpux.py:31-46
# lines [32, 33, 35, 36, 38, 39, 41, 42, 43, 44, 46]
# branches ['35->36', '35->38', '43->44', '43->46']

import pytest
from ansible.module_utils.facts.network.hpux import HPUXNetwork

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.get_bin_path.return_value = '/usr/bin/netstat'
    return mock_module

@pytest.fixture
def mock_get_default_interfaces(mocker):
    return mocker.patch('ansible.module_utils.facts.network.hpux.HPUXNetwork.get_default_interfaces', return_value={'default': 'facts'})

@pytest.fixture
def mock_get_interfaces_info(mocker):
    return mocker.patch('ansible.module_utils.facts.network.hpux.HPUXNetwork.get_interfaces_info', return_value={'eth0': {'key': 'value'}})

def test_hpux_network_populate(mock_module, mock_get_default_interfaces, mock_get_interfaces_info):
    hpux_network = HPUXNetwork(module=mock_module)
    network_facts = hpux_network.populate()

    assert network_facts['default'] == 'facts'
    assert 'eth0' in network_facts['interfaces']
    assert network_facts['eth0'] == {'key': 'value'}
    mock_get_default_interfaces.assert_called_once()
    mock_get_interfaces_info.assert_called_once()
