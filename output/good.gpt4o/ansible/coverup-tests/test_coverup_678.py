# file lib/ansible/module_utils/facts/system/distribution.py:625-628
# lines [625, 626, 627, 628]
# branches []

import pytest
from ansible.module_utils.facts.system.distribution import Distribution

@pytest.fixture
def mock_module(mocker):
    return mocker.Mock()

def test_get_distribution_SMGL(mock_module):
    dist = Distribution(mock_module)
    smgl_facts = dist.get_distribution_SMGL()
    
    assert smgl_facts['distribution'] == 'Source Mage GNU/Linux'
