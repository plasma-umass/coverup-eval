# file: lib/ansible/module_utils/facts/network/generic_bsd.py:172-174
# asked: {"lines": [172, 174], "branches": []}
# gained: {"lines": [172, 174], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

class MockModule:
    pass

class MockNetwork:
    def get_options(self, option_string):
        return option_string.split(',')

@pytest.fixture
def mock_network(monkeypatch):
    module = MockModule()
    network = GenericBsdIfconfigNetwork(module)
    monkeypatch.setattr(network, 'get_options', MockNetwork().get_options)
    return network

def test_parse_options_line(mock_network):
    words = ["option1,option2,option3"]
    current_if = {}
    ips = []

    mock_network.parse_options_line(words, current_if, ips)

    assert 'options' in current_if
    assert current_if['options'] == ["option1", "option2", "option3"]
