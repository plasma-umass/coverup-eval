# file lib/ansible/utils/collection_loader/_collection_finder.py:812-823
# lines [812, 813, 820, 821, 822, 823]
# branches []

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

@pytest.fixture
def cleanup():
    # Setup code if needed
    yield
    # Cleanup code if needed

def test_try_parse_fqcr_valid_ref(cleanup, mocker):
    ref = 'namespace.collection.module_name'
    ref_type = 'module'
    mocker.patch.object(AnsibleCollectionRef, 'from_fqcr', return_value='parsed_ref')
    result = AnsibleCollectionRef.try_parse_fqcr(ref, ref_type)
    assert result == 'parsed_ref'

def test_try_parse_fqcr_invalid_ref(cleanup, mocker):
    ref = 'invalid_ref'
    ref_type = 'module'
    mocker.patch.object(AnsibleCollectionRef, 'from_fqcr', side_effect=ValueError)
    result = AnsibleCollectionRef.try_parse_fqcr(ref, ref_type)
    assert result is None
