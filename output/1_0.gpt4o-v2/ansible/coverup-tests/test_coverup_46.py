# file: lib/ansible/module_utils/facts/network/netbsd.py:23-43
# asked: {"lines": [23, 24, 28, 30, 39, 40, 41, 42, 43], "branches": [[40, 41], [40, 42], [42, 0], [42, 43]]}
# gained: {"lines": [23, 24, 28, 30, 39, 40, 41, 42, 43], "branches": [[40, 41], [40, 42], [42, 0], [42, 43]]}

import pytest
from ansible.module_utils.facts.network.netbsd import NetBSDNetwork
from unittest.mock import MagicMock

@pytest.fixture
def netbsd_network():
    module = MagicMock()
    return NetBSDNetwork(module)

def test_parse_media_line_with_two_words(netbsd_network):
    current_if = {}
    words = ["media:", "Ethernet"]
    netbsd_network.parse_media_line(words, current_if, None)
    assert current_if['media'] == "Ethernet"
    assert 'media_type' not in current_if
    assert 'media_options' not in current_if

def test_parse_media_line_with_three_words(netbsd_network):
    current_if = {}
    words = ["media:", "Ethernet", "10baseT"]
    netbsd_network.parse_media_line(words, current_if, None)
    assert current_if['media'] == "Ethernet"
    assert current_if['media_type'] == "10baseT"
    assert 'media_options' not in current_if

def test_parse_media_line_with_four_words(netbsd_network):
    current_if = {}
    words = ["media:", "Ethernet", "10baseT", "full-duplex"]
    netbsd_network.parse_media_line(words, current_if, None)
    assert current_if['media'] == "Ethernet"
    assert current_if['media_type'] == "10baseT"
    assert current_if['media_options'] == ["full-duplex"]

def test_parse_media_line_with_multiple_options(netbsd_network):
    current_if = {}
    words = ["media:", "Ethernet", "10baseT", "full-duplex,autoselect"]
    netbsd_network.parse_media_line(words, current_if, None)
    assert current_if['media'] == "Ethernet"
    assert current_if['media_type'] == "10baseT"
    assert current_if['media_options'] == ["full-duplex", "autoselect"]
