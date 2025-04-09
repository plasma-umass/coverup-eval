# file lib/ansible/module_utils/facts/network/generic_bsd.py:194-195
# lines [194, 195]
# branches []

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.facts.network.base import Network

@pytest.fixture
def network_instance(mocker):
    mock_module = mocker.Mock()
    return GenericBsdIfconfigNetwork(mock_module)

def test_parse_status_line(network_instance):
    current_if = {}
    words = ["status:", "active"]
    ips = []

    network_instance.parse_status_line(words, current_if, ips)

    assert 'status' in current_if
    assert current_if['status'] == "active"
