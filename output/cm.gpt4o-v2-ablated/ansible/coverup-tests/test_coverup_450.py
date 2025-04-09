# file: lib/ansible/utils/collection_loader/_collection_finder.py:451-463
# asked: {"lines": [453, 459], "branches": [[452, 453], [457, 463], [458, 459]]}
# gained: {"lines": [453, 459], "branches": [[452, 453], [457, 463], [458, 459]]}

import os
import pytest

from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, fullname, source_code_path, subpackage_search_paths, synthetic_filename):
        self._fullname = fullname
        self._source_code_path = source_code_path
        self._subpackage_search_paths = subpackage_search_paths
        self._synthetic_filename = synthetic_filename

    def is_package(self, fullname):
        return fullname == self._fullname

@pytest.fixture
def mock_loader():
    return MockAnsibleCollectionPkgLoaderBase(
        fullname='test_fullname',
        source_code_path='test_source_code_path',
        subpackage_search_paths=['test_subpackage_search_path'],
        synthetic_filename=lambda fullname: 'synthetic_' + fullname
    )

def test_get_filename_correct_fullname(mock_loader):
    filename = mock_loader.get_filename('test_fullname')
    assert filename == 'test_source_code_path'

def test_get_filename_incorrect_fullname(mock_loader):
    with pytest.raises(ValueError) as excinfo:
        mock_loader.get_filename('wrong_fullname')
    assert str(excinfo.value) == 'this loader cannot find files for wrong_fullname, only test_fullname'

def test_get_filename_no_source_code_path_single_search_path(mock_loader, monkeypatch):
    monkeypatch.setattr(mock_loader, '_source_code_path', '')
    filename = mock_loader.get_filename('test_fullname')
    assert filename == os.path.join('test_subpackage_search_path', '__synthetic__')

def test_get_filename_no_source_code_path_multiple_search_paths(mock_loader, monkeypatch):
    monkeypatch.setattr(mock_loader, '_source_code_path', '')
    monkeypatch.setattr(mock_loader, '_subpackage_search_paths', ['path1', 'path2'])
    filename = mock_loader.get_filename('test_fullname')
    assert filename == 'synthetic_test_fullname'
