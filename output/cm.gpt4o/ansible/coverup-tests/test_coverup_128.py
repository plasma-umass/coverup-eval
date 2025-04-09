# file lib/ansible/utils/collection_loader/_collection_finder.py:769-810
# lines [769, 770, 783, 784, 786, 787, 788, 790, 791, 792, 793, 794, 796, 797, 798, 802, 803, 804, 806, 808, 810]
# branches ['783->784', '783->786', '790->791', '790->796', '803->804', '803->806']

import pytest
from unittest import mock
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

# Mocking the to_native and to_text functions
def to_native(value):
    return value

def to_text(value, errors='strict'):
    return value

# Mocking the PB_EXTENSIONS constant
PB_EXTENSIONS = ('.yml', '.yaml')

# Mocking the is_valid_fqcr method
def is_valid_fqcr(ref):
    return True

# Patching the necessary components
@pytest.fixture(autouse=True)
def patch_dependencies(mocker):
    mocker.patch('ansible.utils.collection_loader._collection_finder.to_native', side_effect=to_native)
    mocker.patch('ansible.utils.collection_loader._collection_finder.to_text', side_effect=to_text)
    mocker.patch('ansible.utils.collection_loader._collection_finder.PB_EXTENSIONS', PB_EXTENSIONS)
    mocker.patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef.is_valid_fqcr', side_effect=is_valid_fqcr)

class MockAnsibleCollectionRef:
    def __init__(self, collection_name, subdirs, resource, ref_type):
        self.collection_name = collection_name
        self.subdirs = subdirs
        self.resource = resource
        self.ref_type = ref_type

    @staticmethod
    def is_valid_fqcr(ref):
        return is_valid_fqcr(ref)

@pytest.fixture(autouse=True)
def patch_ansible_collection_ref(mocker):
    mocker.patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef', MockAnsibleCollectionRef)

def test_ansible_collection_ref_from_fqcr_playbook_with_extension():
    ref = 'ns.coll.playbook.yml'
    ref_type = 'playbook'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection_name == 'ns.coll'
    assert result.subdirs == ''
    assert result.resource == 'playbook.yml'
    assert result.ref_type == 'playbook'

def test_ansible_collection_ref_from_fqcr_with_subdirs():
    ref = 'ns.coll.subdir1.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection_name == 'ns.coll'
    assert result.subdirs == 'subdir1'
    assert result.resource == 'resource'
    assert result.ref_type == 'module'

def test_ansible_collection_ref_from_fqcr_without_subdirs():
    ref = 'ns.coll.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection_name == 'ns.coll'
    assert result.subdirs == ''
    assert result.resource == 'resource'
    assert result.ref_type == 'module'
