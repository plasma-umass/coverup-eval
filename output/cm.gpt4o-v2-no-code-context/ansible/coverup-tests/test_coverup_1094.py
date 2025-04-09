# file: lib/ansible/utils/collection_loader/_collection_finder.py:165-179
# asked: {"lines": [], "branches": [[166, 170]]}
# gained: {"lines": [], "branches": [[166, 170]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os

class TestAnsibleCollectionFinder:
    @pytest.fixture(autouse=True)
    def setup_method(self, monkeypatch):
        self.finder = _AnsibleCollectionFinder()
        monkeypatch.setattr(self.finder, '_reload_hack', lambda pkg: None)
        monkeypatch.setattr('os.path.join', lambda *args: '/'.join(args))
        monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.to_native', lambda x: x)

    def test_set_playbook_paths_with_string(self):
        playbook_path = 'test_path'
        self.finder.set_playbook_paths(playbook_path)
        assert self.finder._n_playbook_paths == ['test_path/collections']
        assert self.finder._n_cached_collection_paths is None

    def test_set_playbook_paths_with_list(self):
        playbook_paths = ['test_path1', 'test_path2']
        self.finder.set_playbook_paths(playbook_paths)
        assert self.finder._n_playbook_paths == ['test_path1/collections', 'test_path2/collections']
        assert self.finder._n_cached_collection_paths is None

    def test_set_playbook_paths_with_duplicates(self):
        playbook_paths = ['test_path1', 'test_path2', 'test_path1']
        self.finder.set_playbook_paths(playbook_paths)
        assert self.finder._n_playbook_paths == ['test_path1/collections', 'test_path2/collections']
        assert self.finder._n_cached_collection_paths is None
