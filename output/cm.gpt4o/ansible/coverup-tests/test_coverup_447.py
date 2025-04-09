# file lib/ansible/module_utils/facts/system/distribution.py:559-566
# lines [559, 560, 561, 562, 563, 564, 565, 566]
# branches ['563->564', '563->566']

import pytest
import re
from unittest.mock import Mock

# Assuming the Distribution class is imported from ansible.module_utils.facts.system.distribution
from ansible.module_utils.facts.system.distribution import Distribution

@pytest.fixture
def mock_module(mocker):
    return mocker.Mock()

@pytest.fixture
def distribution(mock_module):
    return Distribution(module=mock_module)

def test_get_distribution_HPUX_no_match(distribution, mock_module):
    mock_module.run_command.return_value = (0, "", "")
    result = distribution.get_distribution_HPUX()
    assert result == {}

def test_get_distribution_HPUX_with_match(distribution, mock_module):
    mock_module.run_command.return_value = (0, "HPUX OE A.11.31.1805", "")
    result = distribution.get_distribution_HPUX()
    assert result == {
        'distribution_version': 'A.11.31',
        'distribution_release': '1805'
    }

def test_get_distribution_HPUX_with_partial_match(distribution, mock_module):
    mock_module.run_command.return_value = (0, "HPUX OE A.11.31", "")
    result = distribution.get_distribution_HPUX()
    assert result == {}

def test_get_distribution_HPUX_command_failure(distribution, mock_module):
    mock_module.run_command.return_value = (1, "", "error")
    result = distribution.get_distribution_HPUX()
    assert result == {}
