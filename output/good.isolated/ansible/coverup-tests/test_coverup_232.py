# file lib/ansible/module_utils/facts/system/distribution.py:381-395
# lines [381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 393, 395]
# branches ['383->384', '383->393', '386->387', '386->388', '389->390', '389->391']

import re
import pytest
from unittest.mock import MagicMock

# Assuming the DistributionFiles class is part of a module named distribution
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_open(mocker):
    mock = mocker.mock_open(read_data='')
    mocker.patch('builtins.open', mock)
    return mock

def test_parse_distribution_file_Mandriva(mocker, mock_open):
    # Prepare the mock data
    data = 'Mandriva\nDISTRIB_RELEASE="2021"\nDISTRIB_CODENAME="Final"'
    mock_open.return_value.read.return_value = data

    # Mock the module parameter required by DistributionFiles
    mock_module = MagicMock()

    # Create an instance of the DistributionFiles class
    distribution_files = DistributionFiles(mock_module)

    # Mock the collected_facts
    collected_facts = {}

    # Call the method with the mock data
    success, mandriva_facts = distribution_files.parse_distribution_file_Mandriva(
        name='MandrivaLinux', data=data, path='/etc/mandriva-release', collected_facts=collected_facts
    )

    # Assertions to ensure the method behaves as expected
    assert success is True
    assert mandriva_facts['distribution'] == 'MandrivaLinux'
    assert mandriva_facts['distribution_version'] == '2021'
    assert mandriva_facts['distribution_release'] == 'Final'

    # Test with data that does not contain 'Mandriva'
    data_without_mandriva = 'SomeOtherDistro\nDISTRIB_RELEASE="2021"\nDISTRIB_CODENAME="Final"'
    success, mandriva_facts = distribution_files.parse_distribution_file_Mandriva(
        name='SomeOtherDistro', data=data_without_mandriva, path='/etc/someother-release', collected_facts=collected_facts
    )

    # Assertions to ensure the method behaves as expected when 'Mandriva' is not in data
    assert success is False
    assert mandriva_facts == {}

    # Clean up / ensure no side effects
    # No need to assert open call, as the method does not open the file directly
