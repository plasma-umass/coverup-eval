# file lib/ansible/plugins/lookup/fileglob.py:56-83
# lines [68, 69, 71, 72, 73, 74]
# branches ['64->68', '68->69', '68->71', '72->73', '72->76', '76->61', '77->76', '80->76']

import os
import pytest
from ansible.plugins.lookup import fileglob
from ansible.errors import AnsibleError

def test_fileglob_lookup_missing_branches(mocker, tmp_path):
    # Setup the test environment
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("content")
    test_dir = tmp_path / "testdir"
    test_dir.mkdir()
    test_dir_file = test_dir / "testfile.txt"
    test_dir_file.write_text("content")

    # Mock the necessary methods and variables
    mocker.patch.object(fileglob.LookupModule, 'find_file_in_search_path', return_value=str(test_dir))
    mocker.patch.object(fileglob.LookupModule, 'get_basedir', return_value=str(tmp_path))
    mocker.patch('os.path.isfile', return_value=True)
    mocker.patch('glob.glob', return_value=[str(test_file)])

    # Create an instance of the LookupModule
    lookup = fileglob.LookupModule()

    # Define the variables with 'ansible_search_path'
    variables_with_search_path = {
        'ansible_search_path': [str(tmp_path)]
    }

    # Define the variables without 'ansible_search_path'
    variables_without_search_path = {}

    # Run the lookup plugin with a term that includes a directory
    results_with_dir = lookup.run([str(test_dir_file)], variables=variables_with_search_path)
    assert results_with_dir == [str(test_file)], "Expected to find the test file in the search path with directory"

    # Run the lookup plugin with a term that does not include a directory and has 'ansible_search_path'
    results_without_dir_with_search_path = lookup.run([test_file.name], variables=variables_with_search_path)
    assert results_without_dir_with_search_path == [str(test_file)], "Expected to find the test file in the search path without directory"

    # Run the lookup plugin with a term that does not include a directory and does not have 'ansible_search_path'
    results_without_dir_without_search_path = lookup.run([test_file.name], variables=variables_without_search_path)
    assert results_without_dir_without_search_path == [str(test_file)], "Expected to find the test file in the base dir without directory"
