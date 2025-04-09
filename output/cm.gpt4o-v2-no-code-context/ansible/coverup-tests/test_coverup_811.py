# file: lib/ansible/utils/collection_loader/_collection_finder.py:448-449
# asked: {"lines": [448, 449], "branches": []}
# gained: {"lines": [448, 449], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self):
        pass

@pytest.fixture
def loader():
    return TestAnsibleCollectionPkgLoaderBase()

def test_synthetic_filename(loader):
    fullname = "some_fullname"
    expected_filename = '<ansible_synthetic_collection_package>'
    result = loader._synthetic_filename(fullname)
    assert result == expected_filename
