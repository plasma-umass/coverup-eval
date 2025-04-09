# file: lib/ansible/modules/apt_repository.py:516-524
# asked: {"lines": [516, 520, 521, 522, 524], "branches": [[520, 521], [520, 524], [521, 520], [521, 522]]}
# gained: {"lines": [516, 520, 521, 522, 524], "branches": [[520, 521], [520, 524], [521, 522]]}

import os
import pytest
from unittest import mock

# Assuming the function revert_sources_list is imported from the module
from ansible.modules.apt_repository import revert_sources_list

@pytest.fixture
def mock_sources():
    sources_before = {'/etc/apt/sources.list': 'content_before'}
    sources_after = {'/etc/apt/sources.list': 'content_after', '/etc/apt/sources.list.d/new_source.list': 'new_content'}
    sourceslist_before = mock.Mock()
    return sources_before, sources_after, sourceslist_before

def test_revert_sources_list_removes_new_files(mock_sources):
    sources_before, sources_after, sourceslist_before = mock_sources

    with mock.patch('os.path.exists', return_value=True) as mock_exists, \
         mock.patch('os.remove') as mock_remove:
        revert_sources_list(sources_before, sources_after, sourceslist_before)
        
        mock_exists.assert_called_with('/etc/apt/sources.list.d/new_source.list')
        mock_remove.assert_called_with('/etc/apt/sources.list.d/new_source.list')
        sourceslist_before.save.assert_called_once()

def test_revert_sources_list_no_new_files(mock_sources):
    sources_before, sources_after, sourceslist_before = mock_sources
    sources_after = sources_before  # No new files

    with mock.patch('os.path.exists') as mock_exists, \
         mock.patch('os.remove') as mock_remove:
        revert_sources_list(sources_before, sources_after, sourceslist_before)
        
        mock_exists.assert_not_called()
        mock_remove.assert_not_called()
        sourceslist_before.save.assert_called_once()
