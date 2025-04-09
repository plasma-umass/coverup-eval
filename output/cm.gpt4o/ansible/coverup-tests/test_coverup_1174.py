# file lib/ansible/modules/apt_repository.py:516-524
# lines [520, 521, 522, 524]
# branches ['520->521', '520->524', '521->520', '521->522']

import os
import pytest
from unittest import mock
from ansible.modules.apt_repository import revert_sources_list

def test_revert_sources_list(mocker):
    # Mock the sources_before and sources_after dictionaries
    sources_before = {'/etc/apt/sources.list': 'content_before'}
    sources_after = {'/etc/apt/sources.list': 'content_before', '/etc/apt/sources.list.d/new_repo.list': 'new_content'}
    
    # Mock the sourceslist_before object
    sourceslist_before = mock.Mock()
    
    # Create a new file to simulate the new repository file
    new_repo_file = '/etc/apt/sources.list.d/new_repo.list'
    with open(new_repo_file, 'w') as f:
        f.write('new_content')
    
    # Ensure the file exists before running the function
    assert os.path.exists(new_repo_file)
    
    # Run the function
    revert_sources_list(sources_before, sources_after, sourceslist_before)
    
    # Assert the new file has been removed
    assert not os.path.exists(new_repo_file)
    
    # Assert the save method was called on sourceslist_before
    sourceslist_before.save.assert_called_once()

    # Clean up any remaining files
    if os.path.exists(new_repo_file):
        os.remove(new_repo_file)
