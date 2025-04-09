# file: lib/ansible/module_utils/facts/collector.py:199-220
# asked: {"lines": [199, 200, 201, 204, 205, 206, 209, 211, 212, 214, 216, 217, 218, 220], "branches": [[204, 205], [204, 220], [206, 204], [206, 209], [211, 212], [211, 214], [216, 206], [216, 217]]}
# gained: {"lines": [199, 200, 201, 204, 205, 206, 209, 211, 212, 214, 216, 217, 218, 220], "branches": [[204, 205], [204, 220], [206, 204], [206, 209], [211, 212], [211, 214], [216, 217]]}

import pytest

class MockCollector:
    def __init__(self, name, platforms):
        self.name = name
        self.platforms = platforms

    def platform_match(self, platform):
        return platform in self.platforms

def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collector import find_collectors_for_platform

    collector1 = MockCollector("collector1", ["linux", "unix"])
    collector2 = MockCollector("collector2", ["windows"])
    collector3 = MockCollector("collector3", ["linux"])
    all_collectors = [collector1, collector2, collector3]

    # Test with a single platform
    result = find_collectors_for_platform(all_collectors, ["linux"])
    assert collector1 in result
    assert collector3 in result
    assert collector2 not in result

    # Test with multiple platforms
    result = find_collectors_for_platform(all_collectors, ["linux", "windows"])
    assert collector1 in result
    assert collector2 in result
    assert collector3 in result

    # Test with no matching platforms
    result = find_collectors_for_platform(all_collectors, ["mac"])
    assert len(result) == 0

    # Test with overlapping platforms
    result = find_collectors_for_platform(all_collectors, ["unix"])
    assert collector1 in result
    assert collector2 not in result
    assert collector3 not in result

    # Test with empty collectors
    result = find_collectors_for_platform([], ["linux"])
    assert len(result) == 0

    # Test with empty platforms
    result = find_collectors_for_platform(all_collectors, [])
    assert len(result) == 0
