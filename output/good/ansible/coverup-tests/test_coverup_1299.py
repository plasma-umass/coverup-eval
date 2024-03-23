# file lib/ansible/modules/apt_repository.py:516-524
# lines [520, 521, 522, 524]
# branches ['520->521', '520->524', '521->520', '521->522']

import os
import pytest
from unittest.mock import MagicMock, patch

# Assuming the existence of a module `ansible.modules.apt_repository` with the function `revert_sources_list`
from ansible.modules.apt_repository import revert_sources_list

def test_revert_sources_list(mocker):
    # Setup
    sources_before = {'/etc/apt/sources.list': 'original_content'}
    sources_after = {'/etc/apt/sources.list': 'new_content', '/etc/apt/sources.list.d/new_repo.list': 'new_repo_content'}
    sourceslist_before = MagicMock()
    
    # Mock os.path.exists to return True for the new file
    mocker.patch('os.path.exists', return_value=True)
    # Mock os.remove to track calls to it
    remove_mock = mocker.patch('os.remove')
    
    # Execute the function under test
    revert_sources_list(sources_before, sources_after, sourceslist_before)
    
    # Assert that os.remove was called for the new file
    remove_mock.assert_called_once_with('/etc/apt/sources.list.d/new_repo.list')
    # Assert that the original sources list was restored
    sourceslist_before.save.assert_called_once()
    
    # Cleanup (not strictly necessary here as we're using mocks, but included for completeness)
    if os.path.exists('/etc/apt/sources.list.d/new_repo.list'):
        os.remove('/etc/apt/sources.list.d/new_repo.list')
