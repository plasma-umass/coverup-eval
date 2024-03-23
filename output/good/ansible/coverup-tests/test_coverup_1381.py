# file lib/ansible/vars/plugins.py:80-95
# lines [86]
# branches ['85->86', '89->93']

import os
import pytest
from ansible.vars.plugins import get_vars_from_inventory_sources
from ansible.parsing.dataloader import DataLoader
from ansible.utils.vars import combine_vars

# Mock function to replace get_vars_from_path
def mock_get_vars_from_path(loader, path, entities, stage):
    return {'mocked_path_var': path}

# Test function to cover missing lines/branches
def test_get_vars_from_inventory_sources_with_none_and_non_dir(mocker):
    # Setup
    loader = DataLoader()
    sources = [None, 'non_existent_file,host1,host2', '/fake/directory']
    entities = []
    stage = None

    # Mock os.path.exists to return False for the non-existent file
    mocker.patch('os.path.exists', return_value=False)
    # Mock os.path.isdir to return False for the non-existent directory
    mocker.patch('os.path.isdir', return_value=False)
    # Mock os.path.dirname to return a fake directory path
    mocker.patch('os.path.dirname', return_value='/fake')
    # Mock combine_vars to use our mock function
    mocker.patch('ansible.vars.plugins.get_vars_from_path', side_effect=mock_get_vars_from_path)

    # Execute the function under test
    data = get_vars_from_inventory_sources(loader, sources, entities, stage)

    # Assertions to verify postconditions
    assert data == {'mocked_path_var': '/fake'}, "The data returned should be from the mocked get_vars_from_path function with the fake directory path"

    # Cleanup is handled by pytest-mock through the mocker fixture
