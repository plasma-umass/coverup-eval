# file lib/ansible/utils/collection_loader/_collection_finder.py:705-760
# lines [705, 713, 714, 715, 716, 717, 719, 720, 722, 723, 725, 726, 727, 728, 729, 731, 733, 734, 736, 737, 739, 741, 742, 743, 744, 747, 749, 750, 751, 753, 755, 757, 759, 760]
# branches ['714->715', '714->716', '719->720', '719->722', '722->723', '722->725', '726->727', '726->731', '727->728', '727->729', '741->742', '741->743', '743->744', '743->747', '749->750', '749->753', '753->755', '753->757']

import pytest
import re
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

# Mock the to_text and to_native functions for testing
def to_text(value, errors=None):
    return str(value)

def to_native(value, errors=None):
    return str(value)

# Apply the mocks to the AnsibleCollectionRef class
AnsibleCollectionRef.to_text = staticmethod(to_text)
AnsibleCollectionRef.to_native = staticmethod(to_native)
AnsibleCollectionRef.VALID_REF_TYPES = ['module', 'role', 'doc_fragment', 'playbook']
AnsibleCollectionRef.VALID_SUBDIRS_RE = re.compile(r'^(\w+\.)*\w+$')
AnsibleCollectionRef.is_valid_collection_name = staticmethod(lambda name: re.match(r'^\w+\.\w+$', name) is not None)

@pytest.fixture
def mock_ansible_collection_ref(mocker):
    mocker.patch.object(AnsibleCollectionRef, 'to_text', side_effect=to_text)
    mocker.patch.object(AnsibleCollectionRef, 'to_native', side_effect=to_native)
    mocker.patch.object(AnsibleCollectionRef, 'VALID_REF_TYPES', ['module', 'role', 'doc_fragment', 'playbook'])
    mocker.patch.object(AnsibleCollectionRef, 'VALID_SUBDIRS_RE', re.compile(r'^(\w+\.)*\w+$'))
    mocker.patch.object(AnsibleCollectionRef, 'is_valid_collection_name', side_effect=lambda name: re.match(r'^\w+\.\w+$', name) is not None)

def test_ansible_collection_ref_invalid_collection_name(mock_ansible_collection_ref):
    with pytest.raises(ValueError) as excinfo:
        AnsibleCollectionRef('invalid/name', None, 'mymodule', 'module')
    assert 'invalid collection name' in str(excinfo.value)

def test_ansible_collection_ref_invalid_ref_type(mock_ansible_collection_ref):
    with pytest.raises(ValueError) as excinfo:
        AnsibleCollectionRef('namespace.collection', None, 'mymodule', 'invalid_type')
    assert 'invalid collection ref_type' in str(excinfo.value)

def test_ansible_collection_ref_invalid_subdirs(mock_ansible_collection_ref):
    with pytest.raises(ValueError) as excinfo:
        AnsibleCollectionRef('namespace.collection', 'invalid/subdirs', 'mymodule', 'module')
    assert 'invalid subdirs entry' in str(excinfo.value)

def test_ansible_collection_ref_valid_with_subdirs(mock_ansible_collection_ref):
    ref = AnsibleCollectionRef('namespace.collection', 'subdir1.subdir2', 'mymodule', 'module')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == 'subdir1.subdir2'
    assert ref.resource == 'mymodule'
    assert ref.ref_type == 'module'
    assert ref.n_python_collection_package_name == 'ansible_collections.namespace.collection'
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.plugins.module.subdir1.subdir2'
    assert ref._fqcr == 'namespace.collection.subdir1.subdir2.mymodule'

def test_ansible_collection_ref_valid_without_subdirs(mock_ansible_collection_ref):
    ref = AnsibleCollectionRef('namespace.collection', None, 'mymodule', 'module')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == ''
    assert ref.resource == 'mymodule'
    assert ref.ref_type == 'module'
    assert ref.n_python_collection_package_name == 'ansible_collections.namespace.collection'
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.plugins.module'
    assert ref._fqcr == 'namespace.collection.mymodule'

def test_ansible_collection_ref_valid_role_type(mock_ansible_collection_ref):
    ref = AnsibleCollectionRef('namespace.collection', None, 'myrole', 'role')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == ''
    assert ref.resource == 'myrole'
    assert ref.ref_type == 'role'
    assert ref.n_python_collection_package_name == 'ansible_collections.namespace.collection'
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.roles.myrole'
    assert ref._fqcr == 'namespace.collection.myrole'

def test_ansible_collection_ref_valid_playbook_type(mock_ansible_collection_ref):
    ref = AnsibleCollectionRef('namespace.collection', None, 'myplaybook', 'playbook')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == ''
    assert ref.resource == 'myplaybook'
    assert ref.ref_type == 'playbook'
    assert ref.n_python_collection_package_name == 'ansible_collections.namespace.collection'
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.playbooks.myplaybook'
    assert ref._fqcr == 'namespace.collection.myplaybook'
