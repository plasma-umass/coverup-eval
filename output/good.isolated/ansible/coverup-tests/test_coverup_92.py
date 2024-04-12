# file lib/ansible/module_utils/common/sys_info.py:112-157
# lines [112, 140, 141, 143, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157]
# branches ['146->147', '146->150', '147->148', '147->150', '148->147', '148->149', '150->151', '150->154', '151->152', '151->154', '152->151', '152->153', '154->155', '154->157']

import pytest
import platform
from ansible.module_utils.common.sys_info import get_platform_subclass

# Mock classes to simulate different platforms and distributions
class BaseClass:
    platform = None
    distribution = None

class LinuxClass(BaseClass):
    platform = 'Linux'

class SpecificLinuxClass(LinuxClass):
    distribution = 'specific-distro'

# Helper function to mock get_all_subclasses
def mock_get_all_subclasses(cls):
    return [LinuxClass, SpecificLinuxClass]

# Helper function to mock get_distribution
def mock_get_distribution():
    return 'specific-distro'

# Test function to improve coverage
def test_get_platform_subclass(mocker):
    mocker.patch('ansible.module_utils.common.sys_info.get_all_subclasses', side_effect=mock_get_all_subclasses)
    mocker.patch('ansible.module_utils.common.sys_info.get_distribution', side_effect=mock_get_distribution)
    mocker.patch('platform.system', return_value='Linux')

    # Test that the correct subclass is returned for a specific distribution
    subclass = get_platform_subclass(BaseClass)
    assert subclass is SpecificLinuxClass

    # Test that the correct subclass is returned when distribution is None
    mocker.patch('ansible.module_utils.common.sys_info.get_distribution', return_value=None)
    subclass = get_platform_subclass(BaseClass)
    assert subclass is LinuxClass

    # Test that the base class is returned when no platform or distribution matches
    mocker.patch('platform.system', return_value='NonExistingPlatform')
    subclass = get_platform_subclass(BaseClass)
    assert subclass is BaseClass
