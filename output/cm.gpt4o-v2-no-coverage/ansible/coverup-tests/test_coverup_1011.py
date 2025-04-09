# file: lib/ansible/module_utils/facts/system/distribution.py:96-97
# asked: {"lines": [96, 97], "branches": []}
# gained: {"lines": [96, 97], "branches": []}

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

class MockModule:
    pass

@pytest.fixture
def mock_module():
    return MockModule()

def test_distribution_files_init(mock_module):
    dist_files = DistributionFiles(mock_module)
    assert dist_files.module == mock_module
