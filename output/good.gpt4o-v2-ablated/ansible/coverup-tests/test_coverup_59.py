# file: lib/ansible/module_utils/facts/collector.py:199-220
# asked: {"lines": [199, 200, 201, 204, 205, 206, 209, 211, 212, 214, 216, 217, 218, 220], "branches": [[204, 205], [204, 220], [206, 204], [206, 209], [211, 212], [211, 214], [216, 206], [216, 217]]}
# gained: {"lines": [199, 200, 201, 204, 205, 206, 209, 211, 212, 214, 216, 217, 218, 220], "branches": [[204, 205], [204, 220], [206, 204], [206, 209], [211, 212], [211, 214], [216, 206], [216, 217]]}

import pytest

class MockCollector:
    def __init__(self, name, platforms):
        self.name = name
        self.platforms = platforms

    @classmethod
    def platform_match(cls, platform):
        return platform in cls.platforms

def test_find_collectors_for_platform(monkeypatch):
    from ansible.module_utils.facts.collector import find_collectors_for_platform

    # Mock collector classes
    class CollectorA(MockCollector):
        name = "CollectorA"
        platforms = ["linux", "unix"]

    class CollectorB(MockCollector):
        name = "CollectorB"
        platforms = ["windows"]

    class CollectorC(MockCollector):
        name = "CollectorC"
        platforms = ["linux"]

    all_collector_classes = [CollectorA, CollectorB, CollectorC]

    # Test case 1: Single compatible platform
    compat_platforms = ["linux"]
    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert found_collectors == {CollectorA, CollectorC}

    # Test case 2: Multiple compatible platforms
    compat_platforms = ["linux", "windows"]
    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert found_collectors == {CollectorA, CollectorB, CollectorC}

    # Test case 3: No compatible platforms
    compat_platforms = ["mac"]
    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert found_collectors == set()

    # Test case 4: Duplicate platform entries
    compat_platforms = ["linux", "linux"]
    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert found_collectors == {CollectorA, CollectorC}
