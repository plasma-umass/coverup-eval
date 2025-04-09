# file: lib/ansible/module_utils/facts/system/distribution.py:510-511
# asked: {"lines": [510, 511], "branches": []}
# gained: {"lines": [510, 511], "branches": []}

import pytest
from ansible.module_utils.facts.system.distribution import Distribution

def test_distribution_init():
    module = "test_module"
    dist = Distribution(module)
    assert dist.module == module
