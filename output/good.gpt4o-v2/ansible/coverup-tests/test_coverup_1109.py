# file: lib/ansible/module_utils/common/sys_info.py:112-157
# asked: {"lines": [140, 141, 143, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157], "branches": [[146, 147], [146, 150], [147, 148], [147, 150], [148, 147], [148, 149], [150, 151], [150, 154], [151, 152], [151, 154], [152, 151], [152, 153], [154, 155], [154, 157]]}
# gained: {"lines": [140, 141, 143, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157], "branches": [[146, 147], [146, 150], [147, 148], [147, 150], [148, 147], [148, 149], [150, 151], [150, 154], [151, 152], [151, 154], [152, 151], [152, 153], [154, 155], [154, 157]]}

import pytest
import platform
from unittest.mock import patch, MagicMock
from ansible.module_utils.common.sys_info import get_platform_subclass

class BaseClass:
    pass

class LinuxSubclass(BaseClass):
    platform = "Linux"
    distribution = None

class WindowsSubclass(BaseClass):
    platform = "Windows"
    distribution = None

class SpecificLinuxSubclass(BaseClass):
    platform = "Linux"
    distribution = "Ubuntu"

def test_get_platform_subclass_linux(monkeypatch):
    monkeypatch.setattr(platform, "system", lambda: "Linux")
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_distribution", lambda: None)
    monkeypatch.setattr("ansible.module_utils.common._utils.get_all_subclasses", lambda cls: {LinuxSubclass, WindowsSubclass})

    result = get_platform_subclass(BaseClass)
    assert result == LinuxSubclass

def test_get_platform_subclass_windows(monkeypatch):
    monkeypatch.setattr(platform, "system", lambda: "Windows")
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_distribution", lambda: None)
    monkeypatch.setattr("ansible.module_utils.common._utils.get_all_subclasses", lambda cls: {LinuxSubclass, WindowsSubclass})

    result = get_platform_subclass(BaseClass)
    assert result == WindowsSubclass

def test_get_platform_subclass_specific_linux(monkeypatch):
    monkeypatch.setattr(platform, "system", lambda: "Linux")
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_distribution", lambda: "Ubuntu")
    monkeypatch.setattr("ansible.module_utils.common._utils.get_all_subclasses", lambda cls: {LinuxSubclass, SpecificLinuxSubclass})

    result = get_platform_subclass(BaseClass)
    assert result == SpecificLinuxSubclass

def test_get_platform_subclass_no_match(monkeypatch):
    monkeypatch.setattr(platform, "system", lambda: "Darwin")
    monkeypatch.setattr("ansible.module_utils.common.sys_info.get_distribution", lambda: None)
    monkeypatch.setattr("ansible.module_utils.common._utils.get_all_subclasses", lambda cls: {LinuxSubclass, WindowsSubclass})

    result = get_platform_subclass(BaseClass)
    assert result == BaseClass
