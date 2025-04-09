# file: lib/ansible/utils/collection_loader/_collection_finder.py:765-767
# asked: {"lines": [765, 766, 767], "branches": []}
# gained: {"lines": [765, 766, 767], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

def test_ansible_collection_ref_fqcr():
    collection_name = 'namespace.collectionname'
    subdirs = 'subdir1.subdir2'
    resource = 'mymodule'
    ref_type = 'modules'
    
    ref = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
    
    assert ref.fqcr == 'namespace.collectionname.subdir1.subdir2.mymodule'
    
    # Clean up
    del ref

def test_ansible_collection_ref_no_subdirs():
    collection_name = 'namespace.collectionname'
    subdirs = None
    resource = 'mymodule'
    ref_type = 'modules'
    
    ref = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
    
    assert ref.fqcr == 'namespace.collectionname.mymodule'
    
    # Clean up
    del ref

def test_ansible_collection_ref_invalid_collection_name():
    collection_name = 'invalid-collection-name'
    subdirs = 'subdir1.subdir2'
    resource = 'mymodule'
    ref_type = 'modules'
    
    with pytest.raises(ValueError, match='invalid collection name'):
        AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)

def test_ansible_collection_ref_invalid_ref_type():
    collection_name = 'namespace.collectionname'
    subdirs = 'subdir1.subdir2'
    resource = 'mymodule'
    ref_type = 'invalid_ref_type'
    
    with pytest.raises(ValueError, match='invalid collection ref_type'):
        AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)

def test_ansible_collection_ref_invalid_subdirs():
    collection_name = 'namespace.collectionname'
    subdirs = 'invalid/subdir'
    resource = 'mymodule'
    ref_type = 'modules'
    
    with pytest.raises(ValueError, match='invalid subdirs entry'):
        AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
