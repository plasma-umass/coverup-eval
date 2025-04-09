# file lib/ansible/module_utils/facts/system/selinux.py:36-39
# lines [36, 37, 38]
# branches []

import pytest
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

def test_selinux_fact_collector_initialization():
    collector = SelinuxFactCollector()
    assert collector.name == 'selinux'
    assert collector._fact_ids == set()

def test_selinux_fact_collector_inheritance():
    collector = SelinuxFactCollector()
    assert isinstance(collector, BaseFactCollector)
