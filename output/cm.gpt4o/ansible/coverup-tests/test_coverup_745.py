# file lib/ansible/module_utils/facts/system/local.py:30-33
# lines [30, 31, 32]
# branches []

import pytest
from ansible.module_utils.facts.system.local import LocalFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

def test_local_fact_collector_initialization():
    collector = LocalFactCollector()
    assert collector.name == 'local'
    assert isinstance(collector, BaseFactCollector)
    assert collector._fact_ids == set()
