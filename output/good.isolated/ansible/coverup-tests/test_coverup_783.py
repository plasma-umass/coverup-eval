# file lib/ansible/utils/collection_loader/_collection_finder.py:765-767
# lines [765, 766, 767]
# branches []

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

class MockAnsibleCollectionRef(AnsibleCollectionRef):
    def __init__(self):
        pass

def test_ansible_collection_ref_fqcr():
    # Create a mock instance of AnsibleCollectionRef and set the _fqcr attribute
    collection_ref = MockAnsibleCollectionRef()
    test_fqcr = "namespace.collection"
    collection_ref._fqcr = test_fqcr

    # Assert that the fqcr property returns the correct value
    assert collection_ref.fqcr == test_fqcr
