# file lib/ansible/utils/collection_loader/_collection_finder.py:705-760
# lines [723, 727, 728, 729, 742, 744, 750, 751, 755]
# branches ['714->716', '722->723', '726->727', '727->728', '727->729', '741->742', '743->744', '749->750', '753->755']

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_text
import re

# Mocking VALID_REF_TYPES and VALID_SUBDIRS_RE for testing purposes
AnsibleCollectionRef.VALID_REF_TYPES = ['module', 'role', 'playbook', 'doc_fragment']
AnsibleCollectionRef.VALID_SUBDIRS_RE = re.compile(r'^[a-zA-Z0-9_]+(\.[a-zA-Z0-9_]+)*$')

def test_ansible_collection_ref_invalid_ref_type():
    with pytest.raises(ValueError, match="invalid collection ref_type: invalid_type"):
        AnsibleCollectionRef('namespace.collection', None, 'resource', 'invalid_type')

def test_ansible_collection_ref_invalid_subdirs():
    with pytest.raises(ValueError, match="invalid subdirs entry: invalid/subdir"):
        AnsibleCollectionRef('namespace.collection', 'invalid/subdir', 'resource', 'module')

def test_ansible_collection_ref_role_type():
    ref = AnsibleCollectionRef('namespace.collection', None, 'resource', 'role')
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.roles.resource'
    assert ref._fqcr == 'namespace.collection.resource'

def test_ansible_collection_ref_playbook_type():
    ref = AnsibleCollectionRef('namespace.collection', None, 'resource', 'playbook')
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.playbooks.resource'
    assert ref._fqcr == 'namespace.collection.resource'

def test_ansible_collection_ref_with_subdirs():
    ref = AnsibleCollectionRef('namespace.collection', 'subdir1.subdir2', 'resource', 'module')
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.plugins.module.subdir1.subdir2'
    assert ref._fqcr == 'namespace.collection.subdir1.subdir2.resource'

def test_ansible_collection_ref_with_subdirs_and_role():
    ref = AnsibleCollectionRef('namespace.collection', 'subdir1.subdir2', 'resource', 'role')
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.roles.subdir1.subdir2.resource'
    assert ref._fqcr == 'namespace.collection.subdir1.subdir2.resource'
