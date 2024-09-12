# file: lib/ansible/module_utils/facts/system/distribution.py:578-587
# asked: {"lines": [578, 579, 580, 581, 582, 583, 584, 585, 586, 587], "branches": [[582, 583], [582, 584], [584, 585], [584, 587]]}
# gained: {"lines": [578, 579, 580, 581, 582, 583, 584, 585, 586, 587], "branches": [[582, 583], [582, 584], [584, 585], [584, 587]]}

import pytest
import platform
import re
from ansible.module_utils.facts.system.distribution import Distribution

@pytest.fixture
def mock_platform_release(mocker):
    return mocker.patch('platform.release')

@pytest.fixture
def mock_platform_version(mocker):
    return mocker.patch('platform.version')

@pytest.fixture
def mock_module(mocker):
    return mocker.Mock()

def test_get_distribution_FreeBSD_release(mock_platform_release, mock_platform_version, mock_module):
    dist = Distribution(mock_module)
    
    # Test case where platform.release() returns a version that matches the regex
    mock_platform_release.return_value = '12.1-RELEASE'
    mock_platform_version.return_value = 'FreeBSD 12.1-RELEASE'
    result = dist.get_distribution_FreeBSD()
    assert result['distribution_release'] == '12.1-RELEASE'
    assert result['distribution_major_version'] == '12'
    assert result['distribution_version'] == '12.1'
    
    # Test case where platform.version() contains 'trueos'
    mock_platform_release.return_value = '12.1-RELEASE'
    mock_platform_version.return_value = 'trueos 12.1-RELEASE'
    result = dist.get_distribution_FreeBSD()
    assert result['distribution_release'] == '12.1-RELEASE'
    assert result['distribution'] == 'TrueOS'
    assert result['distribution_major_version'] == '12'
    assert result['distribution_version'] == '12.1'
    
    # Test case where platform.release() returns a version that does not match the regex
    mock_platform_release.return_value = 'unknown'
    mock_platform_version.return_value = 'FreeBSD unknown'
    result = dist.get_distribution_FreeBSD()
    assert result['distribution_release'] == 'unknown'
    assert 'distribution_major_version' not in result
    assert 'distribution_version' not in result
    assert 'distribution' not in result
