# file: lib/ansible/module_utils/facts/system/distribution.py:578-587
# asked: {"lines": [578, 579, 580, 581, 582, 583, 584, 585, 586, 587], "branches": [[582, 583], [582, 584], [584, 585], [584, 587]]}
# gained: {"lines": [578, 579, 580, 581, 582, 583, 584, 585, 586, 587], "branches": [[582, 583], [582, 584], [584, 585], [584, 587]]}

import pytest
import platform
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.distribution import Distribution

@pytest.fixture
def distribution():
    module = MagicMock()
    return Distribution(module)

def test_get_distribution_FreeBSD_release(distribution):
    with patch('platform.release', return_value='12.1-RELEASE'):
        with patch('platform.version', return_value='FreeBSD 12.1-RELEASE'):
            result = distribution.get_distribution_FreeBSD()
            assert result['distribution_release'] == '12.1-RELEASE'
            assert result['distribution_major_version'] == '12'
            assert result['distribution_version'] == '12.1'
            assert 'distribution' not in result

def test_get_distribution_FreeBSD_trueos(distribution):
    with patch('platform.release', return_value='12.1-RELEASE'):
        with patch('platform.version', return_value='trueos 12.1-RELEASE'):
            result = distribution.get_distribution_FreeBSD()
            assert result['distribution_release'] == '12.1-RELEASE'
            assert result['distribution_major_version'] == '12'
            assert result['distribution_version'] == '12.1'
            assert result['distribution'] == 'TrueOS'

def test_get_distribution_FreeBSD_no_match(distribution):
    with patch('platform.release', return_value='unknown'):
        with patch('platform.version', return_value='FreeBSD unknown'):
            result = distribution.get_distribution_FreeBSD()
            assert result['distribution_release'] == 'unknown'
            assert 'distribution_major_version' not in result
            assert 'distribution_version' not in result
            assert 'distribution' not in result
