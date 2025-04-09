# file: lib/ansible/module_utils/facts/system/distribution.py:96-97
# asked: {"lines": [96, 97], "branches": []}
# gained: {"lines": [96, 97], "branches": []}

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

def test_distribution_files_init():
    module_mock = object()  # Using a simple object as a mock
    dist_files = DistributionFiles(module=module_mock)
    
    assert dist_files.module is module_mock
