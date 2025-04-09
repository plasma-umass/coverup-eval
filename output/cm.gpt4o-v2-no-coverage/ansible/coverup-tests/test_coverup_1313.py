# file: lib/ansible/module_utils/facts/collector.py:199-220
# asked: {"lines": [], "branches": [[216, 206]]}
# gained: {"lines": [], "branches": [[216, 206]]}

import pytest

class MockCollector:
    def __init__(self, name, platforms):
        self.name = name
        self.platforms = platforms

    def platform_match(self, platform):
        return platform in self.platforms

def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collector import find_collectors_for_platform

    collector1 = MockCollector("collector1", ["linux", "windows"])
    collector2 = MockCollector("collector2", ["linux"])
    collector3 = MockCollector("collector3", ["windows"])
    all_collector_classes = [collector1, collector2, collector3]

    # Test with both platforms
    compat_platforms = ["linux", "windows"]
    result = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert result == {collector1, collector2, collector3}

    # Test with only linux
    compat_platforms = ["linux"]
    result = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert result == {collector1, collector2}

    # Test with only windows
    compat_platforms = ["windows"]
    result = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert result == {collector1, collector3}

    # Test with no matching platforms
    compat_platforms = ["mac"]
    result = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert result == set()
