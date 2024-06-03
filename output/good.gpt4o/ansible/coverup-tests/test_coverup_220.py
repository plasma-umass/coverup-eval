# file lib/ansible/module_utils/common/sys_info.py:17-38
# lines [17, 28, 30, 31, 32, 33, 34, 35, 36, 38]
# branches ['30->31', '30->38', '31->32', '31->33', '33->34', '33->35', '35->36', '35->38']

import pytest
import platform
from unittest import mock
from ansible.module_utils.common.sys_info import get_distribution

@pytest.fixture
def mock_distro():
    with mock.patch('ansible.module_utils.common.sys_info.distro') as mock_distro:
        yield mock_distro

@pytest.fixture
def mock_platform():
    with mock.patch('platform.system') as mock_platform:
        yield mock_platform

def test_get_distribution_amzn(mock_distro, mock_platform):
    mock_distro.id.return_value = 'amzn'
    mock_platform.return_value = 'Linux'
    assert get_distribution() == 'Amazon'

def test_get_distribution_rhel(mock_distro, mock_platform):
    mock_distro.id.return_value = 'rhel'
    mock_platform.return_value = 'Linux'
    assert get_distribution() == 'Redhat'

def test_get_distribution_other_linux(mock_distro, mock_platform):
    mock_distro.id.return_value = ''
    mock_platform.return_value = 'Linux'
    assert get_distribution() == 'OtherLinux'

def test_get_distribution_non_linux(mock_distro, mock_platform):
    mock_distro.id.return_value = 'windows'
    mock_platform.return_value = 'Windows'
    assert get_distribution() == 'Windows'
