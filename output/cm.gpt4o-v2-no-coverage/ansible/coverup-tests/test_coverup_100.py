# file: lib/ansible/module_utils/common/sys_info.py:112-157
# asked: {"lines": [112, 140, 141, 143, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157], "branches": [[146, 147], [146, 150], [147, 148], [147, 150], [148, 147], [148, 149], [150, 151], [150, 154], [151, 152], [151, 154], [152, 151], [152, 153], [154, 155], [154, 157]]}
# gained: {"lines": [112, 140, 141, 143, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157], "branches": [[146, 147], [146, 150], [147, 148], [147, 150], [148, 147], [148, 149], [150, 151], [150, 154], [151, 152], [151, 154], [152, 151], [152, 153], [154, 155], [154, 157]]}

import pytest
import platform
from unittest.mock import patch, MagicMock
from ansible.module_utils.common.sys_info import get_platform_subclass
from ansible.module_utils.common._utils import get_all_subclasses

class BaseClass:
    pass

class LinuxSubclass(BaseClass):
    platform = "Linux"
    distribution = None

class WindowsSubclass(BaseClass):
    platform = "Windows"
    distribution = None

class SpecificLinuxSubclass(LinuxSubclass):
    platform = "Linux"
    distribution = "Ubuntu"

@pytest.fixture
def mock_get_all_subclasses():
    with patch('ansible.module_utils.common.sys_info.get_all_subclasses') as mock:
        yield mock

@pytest.fixture
def mock_platform_system():
    with patch('platform.system') as mock:
        yield mock

@pytest.fixture
def mock_get_distribution():
    with patch('ansible.module_utils.common.sys_info.get_distribution') as mock:
        yield mock

def test_get_platform_subclass_no_distribution(mock_get_all_subclasses, mock_platform_system, mock_get_distribution):
    mock_get_all_subclasses.return_value = [LinuxSubclass, WindowsSubclass]
    mock_platform_system.return_value = "Linux"
    mock_get_distribution.return_value = None

    result = get_platform_subclass(BaseClass)
    assert result == LinuxSubclass

def test_get_platform_subclass_with_distribution(mock_get_all_subclasses, mock_platform_system, mock_get_distribution):
    mock_get_all_subclasses.return_value = [LinuxSubclass, WindowsSubclass, SpecificLinuxSubclass]
    mock_platform_system.return_value = "Linux"
    mock_get_distribution.return_value = "Ubuntu"

    result = get_platform_subclass(BaseClass)
    assert result == SpecificLinuxSubclass

def test_get_platform_subclass_fallback_to_base(mock_get_all_subclasses, mock_platform_system, mock_get_distribution):
    mock_get_all_subclasses.return_value = []
    mock_platform_system.return_value = "Linux"
    mock_get_distribution.return_value = None

    result = get_platform_subclass(BaseClass)
    assert result == BaseClass
