# file lib/ansible/module_utils/facts/network/fc_wwn.py:28-31
# lines [28, 29, 30]
# branches []

import pytest
from ansible.module_utils.facts.network.fc_wwn import FcWwnInitiatorFactCollector

def test_fc_wwn_initiator_fact_collector():
    # Create an instance of the class
    collector = FcWwnInitiatorFactCollector()
    
    # Check the name attribute
    assert collector.name == 'fibre_channel_wwn'
    
    # Check the _fact_ids attribute
    assert isinstance(collector._fact_ids, set)
    assert len(collector._fact_ids) == 0
