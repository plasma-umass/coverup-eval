# file lib/ansible/module_utils/facts/system/distribution.py:96-97
# lines [96, 97]
# branches []

import pytest
from unittest.mock import Mock

# Assuming the DistributionFiles class is imported from the correct module
from ansible.module_utils.facts.system.distribution import DistributionFiles

def test_distribution_files_init():
    mock_module = Mock()
    dist_files = DistributionFiles(mock_module)
    
    assert dist_files.module == mock_module
