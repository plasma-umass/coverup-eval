# file lib/ansible/module_utils/common/sys_info.py:41-79
# lines [41, 50, 52, 57, 58, 60, 61, 62, 67, 68, 73, 74, 77, 79]
# branches ['60->61', '60->77', '61->62', '61->79', '67->68', '67->73', '73->74', '73->79']

import pytest
from ansible.module_utils.common.sys_info import get_distribution_version
from unittest.mock import patch

@pytest.fixture
def mock_distro(mocker):
    mocker.patch('ansible.module_utils.common.sys_info.distro.id', return_value='centos')
    mocker.patch('ansible.module_utils.common.sys_info.distro.version', side_effect=['7.5.1804', '7.5'])

def test_get_distribution_version_centos(mock_distro):
    version = get_distribution_version()
    assert version == '7.5', "The version should be the major.minor for CentOS"

@pytest.fixture
def mock_distro_debian(mocker):
    mocker.patch('ansible.module_utils.common.sys_info.distro.id', return_value='debian')
    mocker.patch('ansible.module_utils.common.sys_info.distro.version', side_effect=['10', '10'])

def test_get_distribution_version_debian(mock_distro_debian):
    version = get_distribution_version()
    assert version == '10', "The version should be the major version for Debian"

@pytest.fixture
def mock_distro_unknown(mocker):
    mocker.patch('ansible.module_utils.common.sys_info.distro.id', return_value='unknown')
    mocker.patch('ansible.module_utils.common.sys_info.distro.version', return_value=None)

def test_get_distribution_version_unknown(mock_distro_unknown):
    version = get_distribution_version()
    assert version == '', "The version should be an empty string for unknown distributions"
