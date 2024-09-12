# file: lib/ansible/utils/collection_loader/_collection_finder.py:762-763
# asked: {"lines": [762, 763], "branches": []}
# gained: {"lines": [762, 763], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

def test_ansible_collection_ref_repr():
    collection_name = 'namespace.collectionname'
    subdirs = 'subdir1.subdir2'
    resource = 'mymodule'
    ref_type = 'modules'  # Correct ref_type to match VALID_REF_TYPES
    
    ref = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
    expected_repr = "AnsibleCollectionRef(collection='namespace.collectionname', subdirs='subdir1.subdir2', resource='mymodule')"
    
    assert repr(ref) == expected_repr
