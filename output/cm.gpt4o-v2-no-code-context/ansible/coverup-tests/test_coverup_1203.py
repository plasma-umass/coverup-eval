# file: lib/ansible/module_utils/common/sys_info.py:112-157
# asked: {"lines": [], "branches": [[146, 150]]}
# gained: {"lines": [], "branches": [[146, 150]]}

import pytest
import platform
from ansible.module_utils.common.sys_info import get_platform_subclass

class MockClass:
    platform = None
    distribution = None

def get_all_subclasses(cls):
    return cls.__subclasses__()

def get_distribution():
    return "mock_distribution"

class MockSubclass(MockClass):
    platform = platform.system()
    distribution = "mock_distribution"

class MockSubclassNoDistribution(MockClass):
    platform = platform.system()
    distribution = None

@pytest.fixture
def mock_get_all_subclasses(monkeypatch):
    def mock_subclasses(cls):
        return [MockSubclass, MockSubclassNoDistribution]
    monkeypatch.setattr('ansible.module_utils.common.sys_info.get_all_subclasses', mock_subclasses)

@pytest.fixture
def mock_get_distribution(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.sys_info.get_distribution', lambda: "mock_distribution")

def test_get_platform_subclass_with_distribution(mock_get_all_subclasses, mock_get_distribution):
    result = get_platform_subclass(MockClass)
    assert result == MockSubclass

def test_get_platform_subclass_without_distribution(mock_get_all_subclasses, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.sys_info.get_distribution', lambda: None)
    result = get_platform_subclass(MockClass)
    assert result == MockSubclassNoDistribution

def test_get_platform_subclass_no_matching_subclass(mock_get_all_subclasses, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.sys_info.get_distribution', lambda: None)
    monkeypatch.setattr('ansible.module_utils.common.sys_info.get_all_subclasses', lambda cls: [])
    result = get_platform_subclass(MockClass)
    assert result == MockClass
