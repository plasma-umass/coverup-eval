# file: lib/ansible/module_utils/facts/network/generic_bsd.py:197-198
# asked: {"lines": [197, 198], "branches": []}
# gained: {"lines": [197, 198], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

class TestGenericBsdIfconfigNetwork:
    
    @pytest.fixture
    def network_instance(self, mocker):
        mock_module = mocker.Mock()
        return GenericBsdIfconfigNetwork(mock_module)
    
    def test_parse_lladdr_line(self, network_instance):
        words = ["lladdr", "00:1a:2b:3c:4d:5e"]
        current_if = {}
        ips = []
        
        network_instance.parse_lladdr_line(words, current_if, ips)
        
        assert current_if['lladdr'] == "00:1a:2b:3c:4d:5e"
