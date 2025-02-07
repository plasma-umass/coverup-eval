# file: lib/ansible/module_utils/facts/system/distribution.py:611-623
# asked: {"lines": [611, 612, 613, 614, 615, 616, 617, 618, 619, 621, 622, 623], "branches": [[617, 618], [617, 621]]}
# gained: {"lines": [611, 612, 613, 614, 615, 616, 617, 618, 619, 621, 622, 623], "branches": [[617, 618], [617, 621]]}

import pytest
import platform
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.distribution import Distribution

@pytest.fixture
def distribution():
    module = MagicMock()
    return Distribution(module)

def test_get_distribution_NetBSD_match(distribution):
    with patch('platform.release', return_value='9.1'), \
         patch.object(distribution.module, 'run_command', return_value=(0, 'NetBSD 9.1 (GENERIC)', '')):
        result = distribution.get_distribution_NetBSD()
        assert result['distribution_release'] == '9.1'
        assert result['distribution_major_version'] == '9'
        assert result['distribution_version'] == '9.1'

def test_get_distribution_NetBSD_no_match(distribution):
    with patch('platform.release', return_value='9.1'), \
         patch.object(distribution.module, 'run_command', return_value=(0, 'Some other output', '')):
        result = distribution.get_distribution_NetBSD()
        assert result['distribution_release'] == '9.1'
        assert result['distribution_major_version'] == '9'
        assert result['distribution_version'] == '9.1'
