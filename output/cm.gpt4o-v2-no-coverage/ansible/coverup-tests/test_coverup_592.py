# file: lib/ansible/module_utils/facts/network/sunos.py:106-111
# asked: {"lines": [106, 107, 108, 109, 110, 111], "branches": [[108, 109], [108, 111]]}
# gained: {"lines": [106, 107, 108, 109, 110, 111], "branches": [[108, 109], [108, 111]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.sunos import SunOSNetwork

@pytest.fixture
def sunos_network():
    module = MagicMock()
    return SunOSNetwork(module)

def test_parse_ether_line(sunos_network):
    words = ["ether", "8:0:27:ce:76:fa"]
    current_if = {}
    ips = []

    sunos_network.parse_ether_line(words, current_if, ips)

    assert current_if['macaddress'] == "08:00:27:ce:76:fa"
