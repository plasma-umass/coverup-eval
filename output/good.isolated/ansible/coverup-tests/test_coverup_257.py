# file lib/ansible/module_utils/facts/system/distribution.py:397-406
# lines [397, 398, 399, 400, 401, 402, 403, 404, 405, 406]
# branches ['399->400', '399->406', '401->402', '401->403', '404->399', '404->405']

import re
import pytest

# Assuming the DistributionFiles class is part of a module named distribution
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_collected_facts():
    return {'distribution_version': 'NA'}

def test_parse_distribution_file_NA(mock_collected_facts):
    distribution_files = DistributionFiles(module=None)
    data = 'NAME="TestOS"\nVERSION="1.0"\n'
    name = 'NA'
    path = '/etc/os-release'
    
    success, na_facts = distribution_files.parse_distribution_file_NA(name, data, path, mock_collected_facts)
    
    assert success is True
    assert na_facts['distribution'] == 'TestOS'
    assert na_facts['distribution_version'] == '1.0'
