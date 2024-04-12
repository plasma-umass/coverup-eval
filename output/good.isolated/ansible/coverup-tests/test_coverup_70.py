# file lib/ansible/module_utils/facts/system/distribution.py:167-208
# lines [167, 170, 172, 173, 175, 176, 177, 178, 180, 184, 185, 186, 187, 188, 190, 192, 194, 197, 198, 199, 203, 204, 205, 206, 208]
# branches ['175->176', '175->208', '184->185', '184->190', '190->192', '190->194', '197->175', '197->198']

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

class MockModule:
    def __init__(self):
        self.params = {}

@pytest.fixture
def distribution_files(mocker):
    mock_module = MockModule()
    df = DistributionFiles(module=mock_module)
    mocker.patch.object(df, '_guess_distribution', return_value={})
    mocker.patch.object(df, '_get_dist_file_content')
    mocker.patch.object(df, '_parse_dist_file')
    return df

def test_process_dist_files_allow_empty(distribution_files, mocker):
    # Setup the mock for _get_dist_file_content to return True and some content
    distribution_files._get_dist_file_content.return_value = (True, 'content')
    # Setup the mock for _parse_dist_file to return False and empty facts
    distribution_files._parse_dist_file.return_value = (False, {})
    # Define a mock OSDIST_LIST with allowempty set to True
    mocker.patch.object(distribution_files, 'OSDIST_LIST', [{'name': 'TestOS', 'path': '/etc/test-release', 'allowempty': True}])

    # Call the method under test
    facts = distribution_files.process_dist_files()

    # Assert that the facts are set correctly when allow_empty is True
    assert facts['distribution'] == 'TestOS'
    assert facts['distribution_file_path'] == '/etc/test-release'
    assert facts['distribution_file_variety'] == 'TestOS'

def test_process_dist_files_parsed_file(distribution_files, mocker):
    # Setup the mock for _get_dist_file_content to return True and some content
    distribution_files._get_dist_file_content.return_value = (True, 'content')
    # Setup the mock for _parse_dist_file to return True and some parsed facts
    parsed_facts = {'key': 'value'}
    distribution_files._parse_dist_file.return_value = (True, parsed_facts)
    # Define a mock OSDIST_LIST without allowempty
    mocker.patch.object(distribution_files, 'OSDIST_LIST', [{'name': 'ParsedOS', 'path': '/etc/parsed-release'}])

    # Call the method under test
    facts = distribution_files.process_dist_files()

    # Assert that the facts are set correctly when a parsed file is found
    assert facts['distribution'] == 'ParsedOS'
    assert facts['distribution_file_path'] == '/etc/parsed-release'
    assert facts['distribution_file_variety'] == 'ParsedOS'
    assert facts['distribution_file_parsed'] == True
    assert facts['key'] == 'value'
