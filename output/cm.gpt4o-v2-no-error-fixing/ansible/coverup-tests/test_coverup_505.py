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
    
    assert ref.fqcr == f'{collection_name}.{subdirs}.{resource}'

    # Clean up
    del ref

def test_ansible_collection_ref_fqcr_no_subdirs():
    collection_name = 'namespace.collectionname'
    subdirs = None
    resource = 'mymodule'
    ref_type = 'modules'
    
    ref = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
    
    assert ref.fqcr == f'{collection_name}.{resource}'

    # Clean up
    del ref
