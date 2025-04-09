# file lib/ansible/module_utils/facts/system/distribution.py:600-609
# lines [601, 602, 604, 605, 606, 607, 608, 609]
# branches ['606->607', '606->609']

import pytest
import platform
import re
from unittest.mock import patch, MagicMock

# Assuming the Distribution class is imported from ansible.module_utils.facts.system.distribution
from ansible.module_utils.facts.system.distribution import Distribution

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, "v5.8.2-RELEASE", ""))
    return module

def test_get_distribution_DragonFly(mock_module):
    dist = Distribution(module=mock_module)

    with patch('platform.release', return_value='5.8-RELEASE'):
        dragonfly_facts = dist.get_distribution_DragonFly()

    assert dragonfly_facts['distribution_release'] == '5.8-RELEASE'
    assert dragonfly_facts['distribution_major_version'] == '5'
    assert dragonfly_facts['distribution_version'] == '5.8.2'

    # Ensure run_command was called with the expected command
    mock_module.run_command.assert_called_once_with("/sbin/sysctl -n kern.version")
