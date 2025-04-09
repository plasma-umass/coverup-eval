# file: lib/ansible/module_utils/facts/network/generic_bsd.py:176-178
# asked: {"lines": [176, 178], "branches": []}
# gained: {"lines": [176, 178], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.facts.network.base import Network

class MockModule:
    pass

@pytest.fixture
def network():
    return GenericBsdIfconfigNetwork(MockModule())

def test_parse_nd6_line(network, mocker):
    words = ["nd6", "option1"]
    current_if = {}
    ips = []

    mocker.patch.object(network, 'get_options', return_value="mocked_option")

    network.parse_nd6_line(words, current_if, ips)

    assert current_if['options'] == "mocked_option"
