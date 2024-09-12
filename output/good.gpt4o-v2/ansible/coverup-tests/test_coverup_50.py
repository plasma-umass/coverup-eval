# file: lib/ansible/module_utils/facts/network/hurd.py:32-62
# asked: {"lines": [32, 33, 35, 36, 37, 38, 40, 41, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 62], "branches": [[36, 37], [36, 62], [37, 36], [37, 38], [41, 43], [41, 52], [52, 53], [52, 54], [54, 55], [54, 56], [56, 36], [56, 57]]}
# gained: {"lines": [32, 33, 35, 36, 37, 38, 40, 41, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 62], "branches": [[36, 37], [36, 62], [37, 38], [41, 43], [41, 52], [52, 53], [52, 54], [54, 55], [54, 56], [56, 57]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork

@pytest.fixture
def hurd_pfinet_network():
    return HurdPfinetNetwork(Mock())

def test_assign_network_facts(hurd_pfinet_network):
    network_facts = {}
    fsysopts_path = '/fake/fsysopts'
    socket_path = '/fake/socket'
    
    # Mock the output of the run_command method
    hurd_pfinet_network.module.run_command = Mock(return_value=(0, '--interface=/dev/eth0 --address=192.168.0.1 --netmask=255.255.255.0 --address6=fe80::1/64', ''))
    
    result = hurd_pfinet_network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    
    assert 'interfaces' in result
    assert 'eth0' in result['interfaces']
    assert result['eth0']['active'] is True
    assert result['eth0']['device'] == 'eth0'
    assert result['eth0']['ipv4']['address'] == '192.168.0.1'
    assert result['eth0']['ipv4']['netmask'] == '255.255.255.0'
    assert result['eth0']['ipv6'][0]['address'] == 'fe80::1'
    assert result['eth0']['ipv6'][0]['prefix'] == '64'
