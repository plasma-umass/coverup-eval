# file: lib/ansible/module_utils/facts/system/distribution.py:96-97
# asked: {"lines": [97], "branches": []}
# gained: {"lines": [97], "branches": []}

import pytest

from ansible.module_utils.facts.system.distribution import DistributionFiles

def test_distribution_files_init():
    class MockModule:
        pass

    mock_module = MockModule()
    dist_files = DistributionFiles(mock_module)
    
    assert dist_files.module is mock_module
