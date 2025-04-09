# file lib/ansible/utils/collection_loader/_collection_finder.py:694-704
# lines [694, 696, 702, 703]
# branches []

import pytest
import re
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_text

def test_ansible_collection_ref_valid_ref_types():
    expected_ref_types = frozenset(to_text(r) for r in ['action', 'become', 'cache', 'callback', 'cliconf', 'connection',
                                                        'doc_fragments', 'filter', 'httpapi', 'inventory', 'lookup',
                                                        'module_utils', 'modules', 'netconf', 'role', 'shell', 'strategy',
                                                        'terminal', 'test', 'vars', 'playbook'])
    assert AnsibleCollectionRef.VALID_REF_TYPES == expected_ref_types

def test_ansible_collection_ref_valid_subdirs_re():
    valid_subdirs = ['valid', 'valid.subdir', 'valid.subdir.subsubdir']
    invalid_subdirs = ['invalid-subdir', 'invalid subdir', 'invalid/subdir']

    for subdir in valid_subdirs:
        assert AnsibleCollectionRef.VALID_SUBDIRS_RE.match(to_text(subdir))

    for subdir in invalid_subdirs:
        assert not AnsibleCollectionRef.VALID_SUBDIRS_RE.match(to_text(subdir))

def test_ansible_collection_ref_valid_fqcr_re():
    valid_fqcrs = ['valid.fqcr.name', 'valid.fqcr.name.subname']
    invalid_fqcrs = ['invalid', 'invalid.fqcr', 'invalid.fqcr.']

    for fqcr in valid_fqcrs:
        assert AnsibleCollectionRef.VALID_FQCR_RE.match(to_text(fqcr))

    for fqcr in invalid_fqcrs:
        assert not AnsibleCollectionRef.VALID_FQCR_RE.match(to_text(fqcr))
