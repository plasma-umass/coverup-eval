# file: lib/ansible/modules/apt_repository.py:516-524
# asked: {"lines": [516, 520, 521, 522, 524], "branches": [[520, 521], [520, 524], [521, 520], [521, 522]]}
# gained: {"lines": [516, 520, 521, 522, 524], "branches": [[520, 521], [520, 524], [521, 522]]}

import pytest
import os
from unittest import mock

from ansible.modules.apt_repository import revert_sources_list

def test_revert_sources_list():
    sources_before = {'/etc/apt/sources.list.d/old_repo.list': 'old content'}
    sources_after = {
        '/etc/apt/sources.list.d/old_repo.list': 'old content',
        '/etc/apt/sources.list.d/new_repo.list': 'new content'
    }
    
    class MockSourceList:
        def __init__(self):
            self.saved = False

        def save(self):
            self.saved = True
    
    sourceslist_before = MockSourceList()
    
    with mock.patch('os.path.exists', return_value=True) as mock_exists, \
         mock.patch('os.remove') as mock_remove:
        
        revert_sources_list(sources_before, sources_after, sourceslist_before)
        
        mock_exists.assert_called_once_with('/etc/apt/sources.list.d/new_repo.list')
        mock_remove.assert_called_once_with('/etc/apt/sources.list.d/new_repo.list')
        assert sourceslist_before.saved
