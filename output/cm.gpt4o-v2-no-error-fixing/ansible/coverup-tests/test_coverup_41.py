# file: lib/ansible/module_utils/common/sys_info.py:112-157
# asked: {"lines": [112, 140, 141, 143, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157], "branches": [[146, 147], [146, 150], [147, 148], [147, 150], [148, 147], [148, 149], [150, 151], [150, 154], [151, 152], [151, 154], [152, 151], [152, 153], [154, 155], [154, 157]]}
# gained: {"lines": [112, 140, 141, 143, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157], "branches": [[146, 147], [146, 150], [147, 148], [147, 150], [148, 147], [148, 149], [150, 151], [150, 154], [151, 152], [151, 154], [152, 151], [152, 153], [154, 155], [154, 157]]}

import pytest
import platform
from ansible.module_utils.common.sys_info import get_platform_subclass
from ansible.module_utils.common._utils import get_all_subclasses

class BaseClass:
    platform = None
    distribution = None

class LinuxSubclass(BaseClass):
    platform = "Linux"
    distribution = "Ubuntu"

class WindowsSubclass(BaseClass):
    platform = "Windows"
    distribution = None

def test_get_platform_subclass_linux(monkeypatch):
    def mock_system():
        return "Linux"
    
    def mock_get_distribution():
        return "Ubuntu"
    
    monkeypatch.setattr(platform, "system", mock_system)
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_distribution", mock_get_distribution)
    monkeypatch.setattr("ansible.module_utils.common._utils.get_all_subclasses", lambda cls: {LinuxSubclass, WindowsSubclass})
    
    result = get_platform_subclass(BaseClass)
    assert result == LinuxSubclass

def test_get_platform_subclass_windows(monkeypatch):
    def mock_system():
        return "Windows"
    
    def mock_get_distribution():
        return None
    
    monkeypatch.setattr(platform, "system", mock_system)
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_distribution", mock_get_distribution)
    monkeypatch.setattr("ansible.module_utils.common._utils.get_all_subclasses", lambda cls: {LinuxSubclass, WindowsSubclass})
    
    result = get_platform_subclass(BaseClass)
    assert result == WindowsSubclass

def test_get_platform_subclass_default(monkeypatch):
    def mock_system():
        return "Darwin"
    
    def mock_get_distribution():
        return None
    
    monkeypatch.setattr(platform, "system", mock_system)
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_distribution", mock_get_distribution)
    monkeypatch.setattr("ansible.module_utils.common._utils.get_all_subclasses", lambda cls: {LinuxSubclass, WindowsSubclass})
    
    result = get_platform_subclass(BaseClass)
    assert result == BaseClass
