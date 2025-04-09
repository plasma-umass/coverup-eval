# file lib/ansible/module_utils/common/sys_info.py:41-79
# lines [41, 50, 52, 57, 58, 60, 61, 62, 67, 68, 73, 74, 77, 79]
# branches ['60->61', '60->77', '61->62', '61->79', '67->68', '67->73', '73->74', '73->79']

import pytest
from unittest import mock
import distro
from ansible.module_utils.common.sys_info import get_distribution_version

@pytest.fixture
def mock_distro(mocker):
    mock_distro = mocker.patch('distro.id')
    mock_distro_version = mocker.patch('distro.version')
    return mock_distro, mock_distro_version

def test_get_distribution_version_centos(mock_distro):
    mock_distro, mock_distro_version = mock_distro
    mock_distro.return_value = 'centos'
    mock_distro_version.side_effect = ['7.5.1804', '7.5']

    version = get_distribution_version()
    assert version == '7.5'

def test_get_distribution_version_debian(mock_distro):
    mock_distro, mock_distro_version = mock_distro
    mock_distro.return_value = 'debian'
    mock_distro_version.side_effect = ['10', '10.1']

    version = get_distribution_version()
    assert version == '10.1'

def test_get_distribution_version_other(mock_distro):
    mock_distro, mock_distro_version = mock_distro
    mock_distro.return_value = 'ubuntu'
    mock_distro_version.return_value = '20.04'

    version = get_distribution_version()
    assert version == '20.04'

def test_get_distribution_version_none(mock_distro):
    mock_distro, mock_distro_version = mock_distro
    mock_distro.return_value = 'ubuntu'
    mock_distro_version.return_value = None

    version = get_distribution_version()
    assert version == ''
