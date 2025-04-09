# file: lib/ansible/module_utils/facts/system/distribution.py:625-628
# asked: {"lines": [625, 626, 627, 628], "branches": []}
# gained: {"lines": [625, 626, 627, 628], "branches": []}

import pytest
from ansible.module_utils.facts.system.distribution import Distribution

def test_get_distribution_SMGL():
    distribution = Distribution(module=None)
    smgl_facts = distribution.get_distribution_SMGL()
    assert smgl_facts == {'distribution': 'Source Mage GNU/Linux'}
