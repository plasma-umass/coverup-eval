# file: lib/ansible/utils/collection_loader/_collection_finder.py:812-823
# asked: {"lines": [812, 813, 820, 821, 822, 823], "branches": []}
# gained: {"lines": [812, 813, 820, 821, 822, 823], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

class TestAnsibleCollectionRef:
    
    def test_try_parse_fqcr_success(self, mocker):
        mock_from_fqcr = mocker.patch.object(AnsibleCollectionRef, 'from_fqcr', return_value='parsed_ref')
        ref = 'ns.coll.resource'
        ref_type = 'module'
        
        result = AnsibleCollectionRef.try_parse_fqcr(ref, ref_type)
        
        mock_from_fqcr.assert_called_once_with(ref, ref_type)
        assert result == 'parsed_ref'
    
    def test_try_parse_fqcr_failure(self, mocker):
        mock_from_fqcr = mocker.patch.object(AnsibleCollectionRef, 'from_fqcr', side_effect=ValueError)
        ref = 'invalid.ref'
        ref_type = 'module'
        
        result = AnsibleCollectionRef.try_parse_fqcr(ref, ref_type)
        
        mock_from_fqcr.assert_called_once_with(ref, ref_type)
        assert result is None
