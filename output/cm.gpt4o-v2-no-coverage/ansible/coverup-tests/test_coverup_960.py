# file: lib/ansible/utils/collection_loader/_collection_finder.py:333-334
# asked: {"lines": [333, 334], "branches": []}
# gained: {"lines": [333, 334], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

def test__validate_final():
    # Use a valid fullname to avoid ImportError
    loader = _AnsibleCollectionPkgLoaderBase(fullname="ansible_collections.test.fullname", path_list=[])
    result = loader._validate_final()
    assert result is None
