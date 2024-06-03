# file lib/ansible/module_utils/facts/other/facter.py:26-29
# lines [26, 27, 28]
# branches []

import pytest
from ansible.module_utils.facts.other.facter import FacterFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

def test_facter_fact_collector_initialization():
    collector = FacterFactCollector()
    assert collector.name == 'facter'
    assert collector._fact_ids == {'facter'}
    assert isinstance(collector, BaseFactCollector)
