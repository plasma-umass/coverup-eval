# file lib/ansible/module_utils/facts/system/distribution.py:397-406
# lines [397, 398, 399, 400, 401, 402, 403, 404, 405, 406]
# branches ['399->400', '399->406', '401->402', '401->403', '404->399', '404->405']

import pytest
from unittest.mock import MagicMock

# Assuming the DistributionFiles class is imported from the module
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    module_mock = MagicMock()
    return DistributionFiles(module=module_mock)

def test_parse_distribution_file_NA(distribution_files):
    name = 'NA'
    data = 'NAME="TestDistribution"\nVERSION="1.0"'
    path = '/fake/path'
    collected_facts = {'distribution_version': 'NA'}

    success, na_facts = distribution_files.parse_distribution_file_NA(name, data, path, collected_facts)

    assert success is True
    assert na_facts['distribution'] == 'TestDistribution'
    assert na_facts['distribution_version'] == '1.0'
