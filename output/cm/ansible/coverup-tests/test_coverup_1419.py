# file lib/ansible/utils/collection_loader/_collection_finder.py:844-858
# lines [858]
# branches ['855->858']

import pytest
import re
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_text

# Mock the VALID_FQCR_RE and try_parse_fqcr for testing purposes
AnsibleCollectionRef.VALID_FQCR_RE = re.compile(r'^(\w+\.\w+\.\w+)$')

@pytest.fixture
def mock_try_parse_fqcr(mocker):
    mocker.patch.object(AnsibleCollectionRef, 'try_parse_fqcr', side_effect=lambda ref, ref_type: ref == 'ns.coll.module' and ref_type == 'module')

def test_ansible_collection_ref_is_valid_fqcr_with_ref_type(mock_try_parse_fqcr):
    ref = 'ns.coll.module'
    ref_type = 'module'
    assert AnsibleCollectionRef.is_valid_fqcr(ref, ref_type) == True

def test_ansible_collection_ref_is_valid_fqcr_without_ref_type():
    ref = 'ns.coll.resource'
    assert AnsibleCollectionRef.is_valid_fqcr(ref) == True

def test_ansible_collection_ref_is_valid_fqcr_invalid_format():
    ref = 'invalid_format'
    assert AnsibleCollectionRef.is_valid_fqcr(ref) == False

def test_ansible_collection_ref_is_valid_fqcr_with_ref_type_invalid(mock_try_parse_fqcr):
    ref = 'ns.coll.module'
    ref_type = 'invalid_type'
    assert AnsibleCollectionRef.is_valid_fqcr(ref, ref_type) == False
