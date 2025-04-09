# file lib/ansible/module_utils/facts/system/distribution.py:625-628
# lines [625, 626, 627, 628]
# branches []

import pytest
from ansible.module_utils.facts.system.distribution import Distribution

@pytest.fixture
def distribution_instance(mocker):
    mocker.patch('ansible.module_utils.facts.system.distribution.Distribution.__init__', return_value=None)
    return Distribution()

def test_get_distribution_SMGL(distribution_instance):
    result = distribution_instance.get_distribution_SMGL()
    assert result['distribution'] == 'Source Mage GNU/Linux'
