# file: lib/ansible/module_utils/facts/system/distribution.py:510-511
# asked: {"lines": [510, 511], "branches": []}
# gained: {"lines": [510, 511], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming the Distribution class is defined in ansible/module_utils/facts/system/distribution.py
from ansible.module_utils.facts.system.distribution import Distribution

@pytest.fixture
def mock_module():
    return Mock()

def test_distribution_init(mock_module):
    dist = Distribution(mock_module)
    assert dist.module == mock_module
