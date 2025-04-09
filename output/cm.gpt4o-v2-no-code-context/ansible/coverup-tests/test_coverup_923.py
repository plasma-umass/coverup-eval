# file: lib/ansible/module_utils/facts/network/hurd.py:32-62
# asked: {"lines": [33, 35, 36, 37, 38, 40, 41, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 62], "branches": [[36, 37], [36, 62], [37, 36], [37, 38], [41, 43], [41, 52], [52, 53], [52, 54], [54, 55], [54, 56], [56, 36], [56, 57]]}
# gained: {"lines": [33, 35, 36, 37, 38, 40, 41, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 62], "branches": [[36, 37], [36, 62], [37, 38], [41, 43], [41, 52], [52, 53], [52, 54], [54, 55], [54, 56], [56, 57]]}

import pytest
from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
from ansible.module_utils.facts.network.base import Network

class MockModule:
    def run_command(self, command):
        if command == ['/mock/path/fsysopts', '-L', '/mock/socket']:
            return (0, '--interface=/dev/eth0 --address=192.168.1.1 --netmask=255.255.255.0 --address6=fe80::1/64', '')
        return (1, '', 'error')

@pytest.fixture
def mock_module():
    return MockModule()

@pytest.fixture
def hurd_pfinet_network(mock_module):
    class MockHurdPfinetNetwork(HurdPfinetNetwork):
        def __init__(self, module):
            self.module = module

    return MockHurdPfinetNetwork(mock_module)

def test_assign_network_facts(monkeypatch, hurd_pfinet_network):
    network_facts = {}
    fsysopts_path = '/mock/path/fsysopts'
    socket_path = '/mock/socket'

    result = hurd_pfinet_network.assign_network_facts(network_facts, fsysopts_path, socket_path)

    assert 'interfaces' in result
    assert 'eth0' in result['interfaces']
    assert result['eth0']['active'] is True
    assert result['eth0']['device'] == 'eth0'
    assert result['eth0']['ipv4']['address'] == '192.168.1.1'
    assert result['eth0']['ipv4']['netmask'] == '255.255.255.0'
    assert result['eth0']['ipv6'][0]['address'] == 'fe80::1'
    assert result['eth0']['ipv6'][0]['prefix'] == '64'
