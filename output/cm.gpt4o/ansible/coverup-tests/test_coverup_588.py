# file lib/ansible/utils/collection_loader/_collection_finder.py:812-823
# lines [812, 813, 820, 821, 822, 823]
# branches []

import pytest
from unittest import mock

# Assuming the AnsibleCollectionRef class is defined in ansible.utils.collection_loader._collection_finder
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

@pytest.fixture
def mock_from_fqcr(mocker):
    return mocker.patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef.from_fqcr')

def test_try_parse_fqcr_success(mock_from_fqcr):
    ref = 'ns.coll.resource'
    ref_type = 'module'
    mock_ref_instance = mock.Mock(spec=AnsibleCollectionRef)
    mock_from_fqcr.return_value = mock_ref_instance

    result = AnsibleCollectionRef.try_parse_fqcr(ref, ref_type)

    mock_from_fqcr.assert_called_once_with(ref, ref_type)
    assert result is mock_ref_instance

def test_try_parse_fqcr_failure(mock_from_fqcr):
    ref = 'invalid.ref'
    ref_type = 'module'
    mock_from_fqcr.side_effect = ValueError

    result = AnsibleCollectionRef.try_parse_fqcr(ref, ref_type)

    mock_from_fqcr.assert_called_once_with(ref, ref_type)
    assert result is None
