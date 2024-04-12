# file lib/ansible/module_utils/facts/system/distribution.py:96-97
# lines [96, 97]
# branches []

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

# Mocking the module object that would be passed to DistributionFiles
class MockModule:
    pass

@pytest.fixture
def mock_module(mocker):
    return MockModule()

@pytest.fixture
def distribution_files(mock_module):
    return DistributionFiles(mock_module)

def test_distribution_files_init(distribution_files, mock_module):
    assert distribution_files.module is mock_module, "The module should be correctly assigned to the DistributionFiles instance"

# Cleanup is not necessary in this case as we are not modifying any state outside the scope of the test function.
