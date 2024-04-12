# file lib/ansible/module_utils/facts/network/fc_wwn.py:28-31
# lines [28, 29, 30]
# branches []

import pytest
from ansible.module_utils.facts.network.fc_wwn import FcWwnInitiatorFactCollector

def test_fc_wwn_initiator_fact_collector(mocker):
    mocker.patch.object(FcWwnInitiatorFactCollector, 'collect', return_value={})
    collector = FcWwnInitiatorFactCollector()
    
    assert collector.name == 'fibre_channel_wwn'
    assert collector._fact_ids == set()
    assert collector.collect() == {}
