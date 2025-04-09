# file: lib/ansible/module_utils/facts/network/generic_bsd.py:197-198
# asked: {"lines": [197, 198], "branches": []}
# gained: {"lines": [197, 198], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network_instance(mocker):
    mock_module = mocker.Mock()
    return GenericBsdIfconfigNetwork(mock_module)

def test_parse_lladdr_line(network_instance):
    words = ['lladdr', '00:11:22:33:44:55']
    current_if = {}
    ips = []

    network_instance.parse_lladdr_line(words, current_if, ips)

    assert 'lladdr' in current_if
    assert current_if['lladdr'] == '00:11:22:33:44:55'
