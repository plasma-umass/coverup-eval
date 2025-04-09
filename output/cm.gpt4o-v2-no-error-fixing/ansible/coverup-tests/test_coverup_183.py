# file: lib/ansible/module_utils/facts/system/distribution.py:611-623
# asked: {"lines": [611, 612, 613, 614, 615, 616, 617, 618, 619, 621, 622, 623], "branches": [[617, 618], [617, 621]]}
# gained: {"lines": [611, 612, 613, 614, 615, 616, 617, 618, 619, 621, 622, 623], "branches": [[617, 618], [617, 621]]}

import pytest
from unittest.mock import Mock, patch
import platform
import re

# Assuming the Distribution class is imported from the module
from ansible.module_utils.facts.system.distribution import Distribution

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def distribution(mock_module):
    return Distribution(mock_module)

def test_get_distribution_NetBSD_match(distribution, mock_module):
    mock_module.run_command.return_value = (0, "NetBSD 9.1 (GENERIC)", "")
    with patch.object(platform, 'release', return_value="9.1"):
        result = distribution.get_distribution_NetBSD()
        assert result['distribution_release'] == "9.1"
        assert result['distribution_major_version'] == "9"
        assert result['distribution_version'] == "9.1"

def test_get_distribution_NetBSD_no_match(distribution, mock_module):
    mock_module.run_command.return_value = (0, "Some other version string", "")
    with patch.object(platform, 'release', return_value="9.1"):
        result = distribution.get_distribution_NetBSD()
        assert result['distribution_release'] == "9.1"
        assert result['distribution_major_version'] == "9"
        assert result['distribution_version'] == "9.1"
