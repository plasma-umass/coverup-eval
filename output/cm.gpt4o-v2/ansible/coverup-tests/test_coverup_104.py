# file: lib/ansible/utils/collection_loader/_collection_finder.py:422-446
# asked: {"lines": [422, 423, 424, 429, 432, 434, 436, 437, 438, 439, 440, 443, 444, 446], "branches": [[423, 424], [423, 429], [429, 432], [429, 434], [436, 437], [436, 446], [438, 439], [438, 443], [443, 436], [443, 444]]}
# gained: {"lines": [422, 423, 424, 429, 432, 434, 436, 437, 438, 439, 440, 443, 446], "branches": [[423, 424], [423, 429], [429, 432], [429, 434], [436, 437], [436, 446], [438, 439], [438, 443], [443, 436]]}

import os
import pytest
from ansible.module_utils.common.text.converters import to_bytes
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:
    
    @pytest.fixture
    def loader(self, tmp_path):
        # Create a valid path_list to avoid ImportError
        valid_path = tmp_path / "ansible_collections"
        valid_path.mkdir(parents=True, exist_ok=True)
        return _AnsibleCollectionPkgLoaderBase('ansible_collections.dummy.fullname', [str(valid_path)])

    def test_get_data_no_path(self, loader):
        with pytest.raises(ValueError, match='a path must be specified'):
            loader.get_data('')

    def test_get_data_relative_path(self, loader):
        with pytest.raises(ValueError, match='relative resource paths not supported'):
            loader.get_data('relative/path')

    def test_get_data_file_exists(self, loader, tmp_path):
        test_file = tmp_path / "testfile.txt"
        test_file.write_text("test content")
        
        result = loader.get_data(str(test_file))
        assert result == b"test content"

    def test_get_data_init_py(self, loader, tmp_path):
        test_dir = tmp_path / "testdir"
        test_dir.mkdir()
        init_file = test_dir / "__init__.py"
        init_file.write_text("")

        result = loader.get_data(str(init_file))
        assert result == b""

    def test_get_data_file_not_exists(self, loader, tmp_path):
        test_file = tmp_path / "nonexistentfile.txt"
        
        result = loader.get_data(str(test_file))
        assert result is None
