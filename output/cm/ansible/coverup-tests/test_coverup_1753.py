# file lib/ansible/modules/apt_repository.py:516-524
# lines []
# branches ['521->520']

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.apt_repository import revert_sources_list

@pytest.fixture
def mock_os_path_exists():
    with patch('os.path.exists') as mock:
        yield mock

@pytest.fixture
def mock_os_remove():
    with patch('os.remove') as mock:
        yield mock

@pytest.fixture
def mock_sourceslist_before():
    mock = MagicMock()
    yield mock

def test_revert_sources_list_removes_new_files(mock_os_path_exists, mock_os_remove, mock_sourceslist_before):
    sources_before = {'/etc/apt/sources.list.d/existing_repo.list': 'existing content'}
    sources_after = {
        '/etc/apt/sources.list.d/existing_repo.list': 'existing content',
        '/etc/apt/sources.list.d/new_repo.list': 'new content'
    }
    sourceslist_before = mock_sourceslist_before

    # Set up the mock to simulate the file not existing
    mock_os_path_exists.return_value = False

    revert_sources_list(sources_before, sources_after, sourceslist_before)

    # Check that os.remove was not called since the file does not exist
    mock_os_remove.assert_not_called()

    # Check that the sourceslist_before.save() method was called
    sourceslist_before.save.assert_called_once()
