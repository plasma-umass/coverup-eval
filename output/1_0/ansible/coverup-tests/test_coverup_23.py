# file lib/ansible/module_utils/facts/network/netbsd.py:23-43
# lines [23, 24, 28, 30, 39, 40, 41, 42, 43]
# branches ['40->41', '40->42', '42->exit', '42->43']

import pytest
from ansible.module_utils.facts.network.netbsd import NetBSDNetwork

@pytest.fixture
def netbsd_network(mocker):
    mocker.patch.object(NetBSDNetwork, '__init__', return_value=None)
    netbsd_network = NetBSDNetwork()
    netbsd_network.facts = {}
    return netbsd_network

def test_parse_media_line(netbsd_network):
    current_if = {}
    ips = []

    # Test with only media
    words = ['media:', 'Ethernet']
    netbsd_network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Ethernet'
    assert 'media_type' not in current_if
    assert 'media_options' not in current_if

    # Test with media and media_type
    words = ['media:', 'Ethernet', '10baseT']
    netbsd_network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Ethernet'
    assert current_if['media_type'] == '10baseT'
    assert 'media_options' not in current_if

    # Test with media, media_type, and media_options
    words = ['media:', 'Ethernet', '10baseT', 'full-duplex,multicast']
    netbsd_network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Ethernet'
    assert current_if['media_type'] == '10baseT'
    assert current_if['media_options'] == ['full-duplex', 'multicast']
