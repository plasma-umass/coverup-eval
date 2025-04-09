# file lib/ansible/module_utils/facts/system/platform.py:32-41
# lines [32, 33, 34]
# branches []

import pytest
from ansible.module_utils.facts.system.platform import PlatformFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

def test_platform_fact_collector_initialization():
    collector = PlatformFactCollector()
    assert collector.name == 'platform'
    assert collector._fact_ids == {'system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'}

def test_platform_fact_collector_inheritance():
    collector = PlatformFactCollector()
    assert isinstance(collector, BaseFactCollector)
