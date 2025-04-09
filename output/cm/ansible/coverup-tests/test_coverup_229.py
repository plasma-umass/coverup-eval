# file lib/ansible/module_utils/common/sys_info.py:17-38
# lines [17, 28, 30, 31, 32, 33, 34, 35, 36, 38]
# branches ['30->31', '30->38', '31->32', '31->33', '33->34', '33->35', '35->36', '35->38']

import pytest
from ansible.module_utils.common.sys_info import get_distribution
from unittest.mock import patch
import platform

# Test function to cover the branches in get_distribution
def test_get_distribution(mocker):
    # Mock distro.id() to return 'amzn'
    mocker.patch('ansible.module_utils.common.sys_info.distro.id', return_value='amzn')
    # Mock platform.system() to return 'Linux'
    mocker.patch('ansible.module_utils.common.sys_info.platform.system', return_value='Linux')
    assert get_distribution() == 'Amazon', "Should return 'Amazon' for 'amzn'"

    # Mock distro.id() to return 'rhel'
    mocker.patch('ansible.module_utils.common.sys_info.distro.id', return_value='rhel')
    assert get_distribution() == 'Redhat', "Should return 'Redhat' for 'rhel'"

    # Mock distro.id() to return an empty string
    mocker.patch('ansible.module_utils.common.sys_info.distro.id', return_value='')
    assert get_distribution() == 'OtherLinux', "Should return 'OtherLinux' for an empty string"

    # Mock platform.system() to return a non-Linux system
    mocker.patch('ansible.module_utils.common.sys_info.platform.system', return_value='Windows')
    mocker.patch('ansible.module_utils.common.sys_info.distro.id', return_value='windows')
    assert get_distribution() == 'Windows', "Should return capitalized distro ID for non-Linux systems"
