# file: lib/ansible/utils/collection_loader/_collection_finder.py:422-446
# asked: {"lines": [444], "branches": [[443, 444]]}
# gained: {"lines": [444], "branches": [[443, 444]]}

import os
import pytest
from ansible.module_utils.common.text.converters import to_bytes
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:
    
    @pytest.fixture
    def loader(self):
        return _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.test.fullname', path_list=['/some/path'])
    
    def test_get_data_with_init_py(self, monkeypatch, loader):
        test_path = '/some/path/__init__.py'
        byte_path = to_bytes(test_path)
        
        def mock_isfile(path):
            return False
        
        def mock_isdir(path):
            return path == os.path.dirname(byte_path)
        
        monkeypatch.setattr(os.path, 'isfile', mock_isfile)
        monkeypatch.setattr(os.path, 'isdir', mock_isdir)
        monkeypatch.setattr(os.path, 'dirname', os.path.dirname)
        
        result = loader.get_data(test_path)
        assert result == '', "Expected empty string for __init__.py in existing directory"
    
    def test_get_data_with_nonexistent_file(self, monkeypatch, loader):
        test_path = '/some/nonexistent/path/file.txt'
        
        def mock_isfile(path):
            return False
        
        def mock_isdir(path):
            return False
        
        monkeypatch.setattr(os.path, 'isfile', mock_isfile)
        monkeypatch.setattr(os.path, 'isdir', mock_isdir)
        
        result = loader.get_data(test_path)
        assert result is None, "Expected None for nonexistent file"
