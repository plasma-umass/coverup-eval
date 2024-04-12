# file lib/ansible/module_utils/facts/system/distribution.py:167-208
# lines [192]
# branches ['175->208', '190->192', '197->175']

import pytest
from unittest.mock import MagicMock

# Assuming the DistributionFiles class is part of a module named distribution
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files(mocker):
    module_mock = MagicMock()
    return DistributionFiles(module=module_mock)

@pytest.fixture
def mock_osdist_list():
    return [
        {'name': 'TestOS', 'path': '/etc/test-release', 'allowempty': True},
        {'name': 'AnotherOS', 'path': '/etc/another-release'}
    ]

def test_process_dist_files_with_allow_empty_and_no_dist_file(mocker, distribution_files, mock_osdist_list):
    # Mock the OSDIST_LIST to control the flow
    distribution_files.OSDIST_LIST = mock_osdist_list

    # Mock the _guess_distribution method
    mocker.patch.object(distribution_files, '_guess_distribution', return_value={})

    # Mock the _get_dist_file_content method to simulate the scenario
    # where the first file does not exist and the second file does exist
    # but is not parsed correctly (to cover line 192 and branch 197->175)
    mocker.patch.object(distribution_files, '_get_dist_file_content', side_effect=[
        (False, None),  # First file does not exist
        (True, 'content')  # Second file exists
    ])

    # Mock the _parse_dist_file method to return False, simulating a failure to parse
    mocker.patch.object(distribution_files, '_parse_dist_file', return_value=(False, {}))

    # Run the method under test
    dist_file_facts = distribution_files.process_dist_files()

    # Assert that the method returns the expected facts
    assert 'distribution' not in dist_file_facts
    assert 'distribution_file_path' not in dist_file_facts
    assert 'distribution_file_variety' not in dist_file_facts
    assert 'distribution_file_parsed' not in dist_file_facts

    # Assert that _get_dist_file_content was called twice
    assert distribution_files._get_dist_file_content.call_count == 2

    # Assert that _parse_dist_file was called once
    assert distribution_files._parse_dist_file.call_count == 1
