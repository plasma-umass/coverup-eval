# file lib/ansible/module_utils/facts/collector.py:199-220
# lines [199, 200, 201, 204, 205, 206, 209, 211, 212, 214, 216, 217, 218, 220]
# branches ['204->205', '204->220', '206->204', '206->209', '211->212', '211->214', '216->206', '216->217']

import pytest
from ansible.module_utils.facts.collector import find_collectors_for_platform

class MockCollector:
    def __init__(self, name, platforms):
        self.name = name
        self.platforms = platforms

    @classmethod
    def platform_match(cls, platform):
        return platform in cls.platforms

@pytest.fixture
def mock_collector_classes():
    collector1 = type('Collector1', (MockCollector,), {'name': 'collector1', 'platforms': ['Linux']})
    collector2 = type('Collector2', (MockCollector,), {'name': 'collector2', 'platforms': ['Windows']})
    collector3 = type('Collector3', (MockCollector,), {'name': 'collector3', 'platforms': ['Linux', 'Windows']})
    return [collector1, collector2, collector3]

def test_find_collectors_for_platform(mock_collector_classes):
    compat_platforms = ['Linux']
    found_collectors = find_collectors_for_platform(mock_collector_classes, compat_platforms)
    found_collectors_names = {collector.name for collector in found_collectors}

    assert len(found_collectors) == 2
    assert 'collector1' in found_collectors_names
    assert 'collector3' in found_collectors_names
    assert 'collector2' not in found_collectors_names

    compat_platforms = ['Windows']
    found_collectors = find_collectors_for_platform(mock_collector_classes, compat_platforms)
    found_collectors_names = {collector.name for collector in found_collectors}

    assert len(found_collectors) == 2
    assert 'collector2' in found_collectors_names
    assert 'collector3' in found_collectors_names
    assert 'collector1' not in found_collectors_names

    compat_platforms = ['Darwin']
    found_collectors = find_collectors_for_platform(mock_collector_classes, compat_platforms)
    found_collectors_names = {collector.name for collector in found_collectors}

    assert len(found_collectors) == 0
