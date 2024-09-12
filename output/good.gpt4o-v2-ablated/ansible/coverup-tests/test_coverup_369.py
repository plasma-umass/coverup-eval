# file: lib/ansible/utils/collection_loader/_collection_finder.py:762-763
# asked: {"lines": [762, 763], "branches": []}
# gained: {"lines": [762], "branches": []}

import pytest

from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

@pytest.fixture
def ansible_collection_ref():
    class AnsibleCollectionRef:
        def __init__(self, collection, subdirs, resource):
            self.collection = collection
            self.subdirs = subdirs
            self.resource = resource

        def __repr__(self):
            return 'AnsibleCollectionRef(collection={0!r}, subdirs={1!r}, resource={2!r})'.format(self.collection, self.subdirs, self.resource)

    return AnsibleCollectionRef

def test_ansible_collection_ref_repr(ansible_collection_ref):
    collection = 'test_collection'
    subdirs = ['subdir1', 'subdir2']
    resource = 'test_resource'
    ref = ansible_collection_ref(collection, subdirs, resource)
    expected_repr = "AnsibleCollectionRef(collection='test_collection', subdirs=['subdir1', 'subdir2'], resource='test_resource')"
    assert repr(ref) == expected_repr
