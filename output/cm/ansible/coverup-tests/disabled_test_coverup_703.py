# file lib/ansible/utils/collection_loader/_collection_finder.py:694-704
# lines [694, 696, 702, 703]
# branches []

import pytest
import re
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

def test_ansible_collection_ref_valid_ref_types():
    # Test to ensure VALID_REF_TYPES contains the expected types
    expected_types = {'action', 'become', 'cache', 'callback', 'cliconf', 'connection',
                      'doc_fragments', 'filter', 'httpapi', 'inventory', 'lookup',
                      'module_utils', 'modules', 'netconf', 'role', 'shell', 'strategy',
                      'terminal', 'test', 'vars', 'playbook'}
    assert AnsibleCollectionRef.VALID_REF_TYPES == frozenset(expected_types)

def test_ansible_collection_ref_valid_subdirs_re():
    # Test to ensure VALID_SUBDIRS_RE matches valid subdirectory patterns
    valid_subdirs = ['valid', 'valid.subdir', 'valid.subdir.sub']
    for subdir in valid_subdirs:
        assert AnsibleCollectionRef.VALID_SUBDIRS_RE.match(subdir)

    invalid_subdirs = ['invalid-subdir', 'invalid subdir', '.invalid', 'invalid.']
    for subdir in invalid_subdirs:
        assert not AnsibleCollectionRef.VALID_SUBDIRS_RE.match(subdir)

def test_ansible_collection_ref_valid_fqcr_re():
    # Test to ensure VALID_FQCR_RE matches valid fully qualified collection references
    valid_fqcrs = ['namespace.collection.plugin', 'namespace.collection.subdir.plugin', 'namespace.collection.subdir.subsubdir.plugin']
    for fqcr in valid_fqcrs:
        assert AnsibleCollectionRef.VALID_FQCR_RE.match(fqcr)

    invalid_fqcrs = ['namespace', 'namespace.collection', 'namespace-collection-plugin', 'namespace.collection.']
    for fqcr in invalid_fqcrs:
        assert not AnsibleCollectionRef.VALID_FQCR_RE.match(fqcr)
