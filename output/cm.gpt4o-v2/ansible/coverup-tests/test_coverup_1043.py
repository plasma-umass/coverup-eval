# file: lib/ansible/module_utils/facts/network/generic_bsd.py:194-195
# asked: {"lines": [194, 195], "branches": []}
# gained: {"lines": [194, 195], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from unittest.mock import MagicMock

@pytest.fixture
def network_instance():
    module = MagicMock()
    return GenericBsdIfconfigNetwork(module)

def test_parse_status_line(network_instance):
    words = ["status:", "active"]
    current_if = {}
    ips = []

    network_instance.parse_status_line(words, current_if, ips)

    assert current_if['status'] == "active"
