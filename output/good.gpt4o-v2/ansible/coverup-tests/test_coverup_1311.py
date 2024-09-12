# file: lib/ansible/module_utils/facts/collector.py:199-220
# asked: {"lines": [], "branches": [[216, 206]]}
# gained: {"lines": [], "branches": [[216, 206]]}

import pytest

class MockCollector:
    def __init__(self, name, compatible_platforms):
        self.name = name
        self.compatible_platforms = compatible_platforms

    def platform_match(self, platform):
        return platform in self.compatible_platforms

def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collector import find_collectors_for_platform

    collector1 = MockCollector("collector1", ["linux", "windows"])
    collector2 = MockCollector("collector2", ["linux"])
    collector3 = MockCollector("collector3", ["windows"])
    all_collectors = [collector1, collector2, collector3]

    # Test with a platform that matches multiple collectors
    result = find_collectors_for_platform(all_collectors, ["linux"])
    assert collector1 in result
    assert collector2 in result
    assert collector3 not in result

    # Test with a platform that matches a single collector
    result = find_collectors_for_platform(all_collectors, ["windows"])
    assert collector1 in result
    assert collector2 not in result
    assert collector3 in result

    # Test with a platform that matches no collectors
    result = find_collectors_for_platform(all_collectors, ["mac"])
    assert len(result) == 0

    # Test with multiple platforms
    result = find_collectors_for_platform(all_collectors, ["linux", "windows"])
    assert collector1 in result
    assert collector2 in result
    assert collector3 in result

    # Test with no platforms
    result = find_collectors_for_platform(all_collectors, [])
    assert len(result) == 0
