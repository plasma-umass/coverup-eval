# file: lib/ansible/module_utils/facts/network/hurd.py:85-87
# asked: {"lines": [85, 86, 87], "branches": []}
# gained: {"lines": [85, 86, 87], "branches": []}

import pytest
from ansible.module_utils.facts.network.hurd import HurdNetworkCollector, HurdPfinetNetwork

def test_hurd_network_collector_class_attributes():
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork
