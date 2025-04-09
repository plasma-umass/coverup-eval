# file: lib/ansible/module_utils/facts/system/distribution.py:96-97
# asked: {"lines": [96, 97], "branches": []}
# gained: {"lines": [96, 97], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming the DistributionFiles class is part of a module named distribution
from ansible.module_utils.facts.system.distribution import DistributionFiles

def test_distribution_files_init():
    mock_module = Mock()
    dist_files = DistributionFiles(mock_module)
    
    assert dist_files.module == mock_module
