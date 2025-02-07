# file: lib/ansible/module_utils/facts/system/distribution.py:154-165
# asked: {"lines": [156, 157, 158, 159, 161, 164, 165], "branches": []}
# gained: {"lines": [156, 157, 158, 159, 161, 164, 165], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_distro():
    with patch('ansible.module_utils.common.sys_info.distro') as mock_distro:
        yield mock_distro

@pytest.fixture
def mock_module():
    return MagicMock()

def test_guess_distribution(mock_distro, mock_module):
    mock_distro.id.return_value = 'ubuntu'
    mock_distro.version.return_value = '20.04'
    mock_distro.os_release_info.return_value = {'version_codename': 'focal'}
    mock_distro.lsb_release_info.return_value = {'codename': 'focal'}
    mock_distro.codename.return_value = 'focal'

    dist_files = DistributionFiles(mock_module)
    result = dist_files._guess_distribution()

    assert result['distribution'] == 'Ubuntu'
    assert result['distribution_version'] == '20.04'
    assert result['distribution_release'] == 'focal'
    assert result['distribution_major_version'] == '20'

def test_guess_distribution_no_codename(mock_distro, mock_module):
    mock_distro.id.return_value = 'ubuntu'
    mock_distro.version.return_value = '20.04'
    mock_distro.os_release_info.return_value = {}
    mock_distro.lsb_release_info.return_value = {}
    mock_distro.codename.return_value = None

    dist_files = DistributionFiles(mock_module)
    result = dist_files._guess_distribution()

    assert result['distribution'] == 'Ubuntu'
    assert result['distribution_version'] == '20.04'
    assert result['distribution_release'] == 'NA'
    assert result['distribution_major_version'] == '20'

def test_guess_distribution_no_version(mock_distro, mock_module):
    mock_distro.id.return_value = 'ubuntu'
    mock_distro.version.return_value = ''
    mock_distro.os_release_info.return_value = {'version_codename': 'focal'}
    mock_distro.lsb_release_info.return_value = {'codename': 'focal'}
    mock_distro.codename.return_value = 'focal'

    dist_files = DistributionFiles(mock_module)
    result = dist_files._guess_distribution()

    assert result['distribution'] == 'Ubuntu'
    assert result['distribution_version'] == 'NA'
    assert result['distribution_release'] == 'focal'
    assert result['distribution_major_version'] == 'NA'
