# file: lib/ansible/module_utils/common/sys_info.py:112-157
# asked: {"lines": [140, 141, 143, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157], "branches": [[146, 147], [146, 150], [147, 148], [147, 150], [148, 147], [148, 149], [150, 151], [150, 154], [151, 152], [151, 154], [152, 151], [152, 153], [154, 155], [154, 157]]}
# gained: {"lines": [140, 141, 143, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157], "branches": [[146, 147], [147, 148], [147, 150], [148, 147], [148, 149], [150, 151], [150, 154], [151, 152], [151, 154], [152, 151], [152, 153], [154, 155], [154, 157]]}

import pytest
import platform
from ansible.module_utils.common.sys_info import get_platform_subclass

class MockClass:
    platform = None
    distribution = None

def get_distribution():
    return "mock_distribution"

def get_all_subclasses(cls):
    class SubClass1(cls):
        platform = platform.system()
        distribution = "mock_distribution"
    
    class SubClass2(cls):
        platform = platform.system()
        distribution = None
    
    class SubClass3(cls):
        platform = "OtherPlatform"
        distribution = "mock_distribution"
    
    return [SubClass1, SubClass2, SubClass3]

@pytest.fixture
def mock_platform_system(monkeypatch):
    monkeypatch.setattr(platform, "system", lambda: "MockPlatform")

@pytest.fixture
def mock_get_distribution(monkeypatch):
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_distribution", get_distribution)

@pytest.fixture
def mock_get_all_subclasses(monkeypatch):
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_all_subclasses", get_all_subclasses)

def test_get_platform_subclass_distribution_match(mock_platform_system, mock_get_distribution, mock_get_all_subclasses):
    subclass = get_platform_subclass(MockClass)
    assert subclass.distribution == "mock_distribution"
    assert subclass.platform == "MockPlatform"

def test_get_platform_subclass_no_distribution_match(mock_platform_system, mock_get_distribution, mock_get_all_subclasses, monkeypatch):
    def get_all_subclasses_no_distribution(cls):
        class SubClass1(cls):
            platform = platform.system()
            distribution = None
        
        class SubClass2(cls):
            platform = "OtherPlatform"
            distribution = "mock_distribution"
        
        return [SubClass1, SubClass2]
    
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_all_subclasses", get_all_subclasses_no_distribution)
    subclass = get_platform_subclass(MockClass)
    assert subclass.distribution is None
    assert subclass.platform == "MockPlatform"

def test_get_platform_subclass_no_match(mock_platform_system, mock_get_distribution, mock_get_all_subclasses, monkeypatch):
    def get_all_subclasses_no_match(cls):
        class SubClass1(cls):
            platform = "OtherPlatform"
            distribution = "other_distribution"
        
        return [SubClass1]
    
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_all_subclasses", get_all_subclasses_no_match)
    subclass = get_platform_subclass(MockClass)
    assert subclass == MockClass
