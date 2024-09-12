# file: lib/ansible/module_utils/facts/network/base.py:22-40
# asked: {"lines": [22, 23, 32, 35, 36, 39, 40], "branches": []}
# gained: {"lines": [22, 23, 32, 35, 36, 39, 40], "branches": []}

import pytest
from ansible.module_utils.facts.network.base import Network

class TestNetwork:
    
    def test_network_init(self):
        module = object()
        network = Network(module)
        assert network.module == module

    def test_network_init_with_load_on_init(self):
        module = object()
        network = Network(module, load_on_init=True)
        assert network.module == module

    def test_network_populate(self):
        module = object()
        network = Network(module)
        result = network.populate()
        assert result == {}
