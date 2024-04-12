# file lib/ansible/module_utils/facts/collector.py:199-220
# lines []
# branches ['216->206']

import pytest
from ansible.module_utils.facts.collector import find_collectors_for_platform

class MockCollector:
    def __init__(self, name, match):
        self.name = name
        self.match = match

    def platform_match(self, compat_platform):
        return self.match

@pytest.fixture
def mock_collector_classes():
    return [
        MockCollector('collector1', True),
        MockCollector('collector2', False),
        MockCollector('collector1', True)  # Duplicate name, should not be added again
    ]

def test_find_collectors_for_platform(mock_collector_classes):
    compat_platforms = ['test_platform']
    found_collectors = find_collectors_for_platform(mock_collector_classes, compat_platforms)
    
    # Verify that only the collectors that match the platform are added
    assert len(found_collectors) == 1
    assert any(collector.name == 'collector1' for collector in found_collectors)
    
    # Verify that collectors with duplicate names are not added again
    found_collectors_names = {collector.name for collector in found_collectors}
    assert len(found_collectors_names) == 1
    assert 'collector1' in found_collectors_names
