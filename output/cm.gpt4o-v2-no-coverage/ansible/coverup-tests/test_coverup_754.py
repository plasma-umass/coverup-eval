# file: lib/ansible/module_utils/facts/system/distribution.py:625-628
# asked: {"lines": [625, 626, 627, 628], "branches": []}
# gained: {"lines": [625, 626, 627, 628], "branches": []}

import pytest
from ansible.module_utils.facts.system.distribution import Distribution

class MockModule:
    pass

def test_get_distribution_SMGL():
    mock_module = MockModule()
    dist = Distribution(mock_module)
    result = dist.get_distribution_SMGL()
    assert result == {'distribution': 'Source Mage GNU/Linux'}
