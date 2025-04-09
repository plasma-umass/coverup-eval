# file: lib/ansible/utils/collection_loader/_collection_finder.py:411-420
# asked: {"lines": [413, 415, 419, 420], "branches": [[412, 413], [414, 415], [416, 419]]}
# gained: {"lines": [413, 415, 419, 420], "branches": [[412, 413], [414, 415], [416, 419]]}

import pytest
from unittest.mock import MagicMock

from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def loader():
    loader = _AnsibleCollectionPkgLoaderBase(fullname="ansible_collections.test.fullname", path_list=["/fake/path"])
    loader._fullname = "ansible_collections.test.fullname"
    loader._source_code_path = "test/path"
    loader._decoded_source = None
    return loader

def test_get_source_with_cached_source(loader):
    loader._decoded_source = "cached source"
    assert loader.get_source("ansible_collections.test.fullname") == "cached source"

def test_get_source_with_different_fullname(loader):
    with pytest.raises(ValueError, match="this loader cannot load source for test.wrongname, only ansible_collections.test.fullname"):
        loader.get_source("test.wrongname")

def test_get_source_with_no_source_code_path(loader, mocker):
    loader._source_code_path = None
    assert loader.get_source("ansible_collections.test.fullname") is None

def test_get_source_with_source_code_path(loader, mocker):
    mocker.patch.object(loader, 'get_data', return_value="decoded source")
    assert loader.get_source("ansible_collections.test.fullname") == "decoded source"
    loader.get_data.assert_called_once_with("test/path")
    assert loader._decoded_source == "decoded source"
