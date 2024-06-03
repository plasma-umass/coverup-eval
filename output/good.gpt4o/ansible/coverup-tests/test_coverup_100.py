# file lib/ansible/module_utils/common/sys_info.py:112-157
# lines [112, 140, 141, 143, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157]
# branches ['146->147', '146->150', '147->148', '147->150', '148->147', '148->149', '150->151', '150->154', '151->152', '151->154', '152->151', '152->153', '154->155', '154->157']

import pytest
import platform
from unittest.mock import patch, MagicMock
from ansible.module_utils.common.sys_info import get_platform_subclass

class BaseClass:
    platform = None
    distribution = None

class LinuxClass(BaseClass):
    platform = 'Linux'
    distribution = None

class UbuntuClass(BaseClass):
    platform = 'Linux'
    distribution = 'Ubuntu'

class WindowsClass(BaseClass):
    platform = 'Windows'
    distribution = None

def get_all_subclasses(cls):
    return cls.__subclasses__()

@pytest.fixture
def mock_get_all_subclasses(mocker):
    mocker.patch('ansible.module_utils.common.sys_info.get_all_subclasses', side_effect=get_all_subclasses)

@pytest.fixture
def mock_get_distribution(mocker):
    return mocker.patch('ansible.module_utils.common.sys_info.get_distribution')

@pytest.fixture
def mock_platform_system(mocker):
    return mocker.patch('platform.system')

def test_get_platform_subclass_linux(mock_get_all_subclasses, mock_get_distribution, mock_platform_system):
    mock_platform_system.return_value = 'Linux'
    mock_get_distribution.return_value = None

    subclass = get_platform_subclass(BaseClass)
    assert subclass == LinuxClass

def test_get_platform_subclass_ubuntu(mock_get_all_subclasses, mock_get_distribution, mock_platform_system):
    mock_platform_system.return_value = 'Linux'
    mock_get_distribution.return_value = 'Ubuntu'

    subclass = get_platform_subclass(BaseClass)
    assert subclass == UbuntuClass

def test_get_platform_subclass_windows(mock_get_all_subclasses, mock_get_distribution, mock_platform_system):
    mock_platform_system.return_value = 'Windows'
    mock_get_distribution.return_value = None

    subclass = get_platform_subclass(BaseClass)
    assert subclass == WindowsClass

def test_get_platform_subclass_default(mock_get_all_subclasses, mock_get_distribution, mock_platform_system):
    mock_platform_system.return_value = 'UnknownOS'
    mock_get_distribution.return_value = None

    subclass = get_platform_subclass(BaseClass)
    assert subclass == BaseClass
