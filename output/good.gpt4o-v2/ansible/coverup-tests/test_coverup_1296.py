# file: lib/ansible/module_utils/facts/network/hurd.py:32-62
# asked: {"lines": [], "branches": [[37, 36], [56, 36]]}
# gained: {"lines": [], "branches": [[37, 36]]}

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork

@pytest.fixture
def hurd_pfinet_network():
    module = Mock()
    return HurdPfinetNetwork(module)

def test_assign_network_facts_no_equals(hurd_pfinet_network, monkeypatch):
    network_facts = {}
    fsysopts_path = '/fake/fsysopts'
    socket_path = '/fake/socket'
    
    def mock_run_command(cmd):
        return (0, '--interface', '')

    monkeypatch.setattr(hurd_pfinet_network.module, 'run_command', mock_run_command)
    result = hurd_pfinet_network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    
    assert result['interfaces'] == []

def test_assign_network_facts_no_double_dash(hurd_pfinet_network, monkeypatch):
    network_facts = {}
    fsysopts_path = '/fake/fsysopts'
    socket_path = '/fake/socket'
    
    def mock_run_command(cmd):
        return (0, 'interface=eth0', '')

    monkeypatch.setattr(hurd_pfinet_network.module, 'run_command', mock_run_command)
    result = hurd_pfinet_network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    
    assert result['interfaces'] == []

def test_assign_network_facts_interface(hurd_pfinet_network, monkeypatch):
    network_facts = {}
    fsysopts_path = '/fake/fsysopts'
    socket_path = '/fake/socket'
    
    def mock_run_command(cmd):
        return (0, '--interface=/dev/eth0', '')

    monkeypatch.setattr(hurd_pfinet_network.module, 'run_command', mock_run_command)
    result = hurd_pfinet_network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    
    assert 'eth0' in result['interfaces']
    assert result['eth0']['device'] == 'eth0'
    assert result['eth0']['active'] is True

def test_assign_network_facts_address(hurd_pfinet_network, monkeypatch):
    network_facts = {}
    fsysopts_path = '/fake/fsysopts'
    socket_path = '/fake/socket'
    
    def mock_run_command(cmd):
        return (0, '--interface=/dev/eth0 --address=192.168.0.1', '')

    monkeypatch.setattr(hurd_pfinet_network.module, 'run_command', mock_run_command)
    result = hurd_pfinet_network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    
    assert result['eth0']['ipv4']['address'] == '192.168.0.1'

def test_assign_network_facts_netmask(hurd_pfinet_network, monkeypatch):
    network_facts = {}
    fsysopts_path = '/fake/fsysopts'
    socket_path = '/fake/socket'
    
    def mock_run_command(cmd):
        return (0, '--interface=/dev/eth0 --netmask=255.255.255.0', '')

    monkeypatch.setattr(hurd_pfinet_network.module, 'run_command', mock_run_command)
    result = hurd_pfinet_network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    
    assert result['eth0']['ipv4']['netmask'] == '255.255.255.0'

def test_assign_network_facts_address6(hurd_pfinet_network, monkeypatch):
    network_facts = {}
    fsysopts_path = '/fake/fsysopts'
    socket_path = '/fake/socket'
    
    def mock_run_command(cmd):
        return (0, '--interface=/dev/eth0 --address6=fe80::1/64', '')

    monkeypatch.setattr(hurd_pfinet_network.module, 'run_command', mock_run_command)
    result = hurd_pfinet_network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    
    assert result['eth0']['ipv6'][0]['address'] == 'fe80::1'
    assert result['eth0']['ipv6'][0]['prefix'] == '64'
