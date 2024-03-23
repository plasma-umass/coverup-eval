# file lib/ansible/utils/collection_loader/_collection_finder.py:158-163
# lines [158, 159, 160, 161, 162, 163]
# branches ['161->162', '161->163']

import pytest
from ansible.utils.collection_loader import _collection_finder

# Mock the _AnsibleCollectionFinder class to control the _n_playbook_paths and _n_configured_paths attributes
class MockAnsibleCollectionFinder(_collection_finder._AnsibleCollectionFinder):
    def __init__(self):
        self._n_cached_collection_paths = None
        self._n_playbook_paths = []
        self._n_configured_paths = []

# Test function to cover the missing lines/branches in the _n_collection_paths property
def test_n_collection_paths():
    finder = MockAnsibleCollectionFinder()

    # Initially, there should be no cached paths, so the property should combine playbook and configured paths
    assert finder._n_collection_paths == []
    assert finder._n_cached_collection_paths == []

    # Now set some paths and check if they are returned by the property
    finder._n_playbook_paths = ['playbook_path']
    finder._n_configured_paths = ['configured_path']
    assert finder._n_collection_paths == ['playbook_path', 'configured_path']
    assert finder._n_cached_collection_paths == ['playbook_path', 'configured_path']

    # After the paths are cached, changing the original lists should not affect the property
    finder._n_playbook_paths.append('new_playbook_path')
    finder._n_configured_paths.append('new_configured_path')
    assert finder._n_collection_paths == ['playbook_path', 'configured_path']
    assert finder._n_cached_collection_paths == ['playbook_path', 'configured_path']
