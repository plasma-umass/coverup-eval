# file lib/ansible/module_utils/facts/system/platform.py:32-41
# lines [32, 33, 34]
# branches []

import pytest
from ansible.module_utils.facts.system.platform import PlatformFactCollector

# Since the PlatformFactCollector class does not contain any methods,
# we will create a test that simply instantiates the class and checks its attributes.

def test_platform_fact_collector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == set([
        'system',
        'kernel',
        'kernel_version',
        'machine',
        'python_version',
        'architecture',
        'machine_id'
    ])
