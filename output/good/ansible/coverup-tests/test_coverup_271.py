# file lib/ansible/utils/collection_loader/_collection_finder.py:411-420
# lines [411, 412, 413, 414, 415, 416, 417, 419, 420]
# branches ['412->413', '412->414', '414->415', '414->416', '416->417', '416->419']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockLoader(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, fullname, source_code_path=None):
        self._fullname = fullname
        self._source_code_path = source_code_path
        self._decoded_source = None

    def get_data(self, path):
        return b"mocked data"

@pytest.fixture
def mock_loader():
    return MockLoader(fullname="test.module", source_code_path="/fake/path/to/source.py")

def test_get_source_with_decoded_source(mock_loader):
    # Set the decoded source to simulate it being loaded already
    mock_loader._decoded_source = "already loaded source"
    assert mock_loader.get_source("test.module") == "already loaded source"

def test_get_source_with_fullname_mismatch(mock_loader):
    with pytest.raises(ValueError):
        mock_loader.get_source("wrong.module")

def test_get_source_with_no_source_code_path(mock_loader):
    mock_loader._source_code_path = None
    assert mock_loader.get_source("test.module") is None

def test_get_source_with_source_code_path(mock_loader):
    assert mock_loader.get_source("test.module") == b"mocked data"
    assert mock_loader._decoded_source == b"mocked data"
