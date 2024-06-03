# file lib/ansible/module_utils/facts/system/distribution.py:513-545
# lines [513, 514, 519, 520, 521, 522, 524, 526, 527, 528, 529, 530, 531, 533, 536, 538, 540, 543, 545]
# branches ['526->527', '526->531', '531->533', '531->540']

import pytest
import platform
from unittest.mock import patch, MagicMock

# Assuming the Distribution class is imported from ansible.module_utils.facts.system.distribution
from ansible.module_utils.facts.system.distribution import Distribution

@pytest.fixture
def mock_platform_system():
    with patch('platform.system') as mock_system:
        yield mock_system

@pytest.fixture
def mock_platform_release():
    with patch('platform.release') as mock_release:
        yield mock_release

@pytest.fixture
def mock_platform_version():
    with patch('platform.version') as mock_version:
        yield mock_version

@pytest.fixture
def mock_distribution_files():
    with patch('ansible.module_utils.facts.system.distribution.DistributionFiles') as mock_dist_files:
        yield mock_dist_files

@pytest.fixture
def mock_linux_distribution():
    with patch('ansible.module_utils.facts.system.distribution.LinuxDistribution') as mock_linux_dist:
        yield mock_linux_dist

def test_get_distribution_facts_linux(mock_platform_system, mock_platform_release, mock_platform_version, mock_distribution_files):
    mock_platform_system.return_value = 'Linux'
    mock_platform_release.return_value = '5.4.0-42-generic'
    mock_platform_version.return_value = '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020'
    
    mock_dist_files_instance = MagicMock()
    mock_distribution_files.return_value = mock_dist_files_instance
    mock_dist_files_instance.process_dist_files.return_value = {
        'distribution': 'Ubuntu',
        'distribution_release': '20.04',
        'distribution_version': 'Focal Fossa'
    }
    
    dist = Distribution(module=MagicMock())
    dist.OS_FAMILY = {'Ubuntu': 'Debian'}
    
    facts = dist.get_distribution_facts()
    
    assert facts['distribution'] == 'Ubuntu'
    assert facts['distribution_release'] == '20.04'
    assert facts['distribution_version'] == 'Focal Fossa'
    assert facts['os_family'] == 'Debian'

def test_get_distribution_facts_aix(mock_platform_system, mock_platform_release, mock_platform_version):
    mock_platform_system.return_value = 'AIX'
    mock_platform_release.return_value = '7.2'
    mock_platform_version.return_value = '1'
    
    dist = Distribution(module=MagicMock())
    dist.OS_FAMILY = {}
    
    def mock_get_distribution_AIX():
        return {
            'distribution': 'AIX',
            'distribution_release': '7.2',
            'distribution_version': '1'
        }
    
    dist.get_distribution_AIX = mock_get_distribution_AIX
    
    facts = dist.get_distribution_facts()
    
    assert facts['distribution'] == 'AIX'
    assert facts['distribution_release'] == '7.2'
    assert facts['distribution_version'] == '1'
    assert facts['os_family'] == 'AIX'
