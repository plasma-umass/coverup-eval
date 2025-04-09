# file: lib/ansible/utils/collection_loader/_collection_finder.py:844-858
# asked: {"lines": [844, 845, 853, 855, 856, 858], "branches": [[855, 856], [855, 858]]}
# gained: {"lines": [844, 845, 853, 855, 856, 858], "branches": [[855, 856], [855, 858]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils.common.text.converters import to_text

class TestAnsibleCollectionRef:
    
    @pytest.mark.parametrize("ref, ref_type, expected", [
        ("namespace.collection.resource", None, True),
        ("namespace.collection.subdir.resource", None, True),
        ("namespace.collection", None, False),
        ("namespace.collection.resource", "module", False),  # Assuming try_parse_fqcr returns None
    ])
    def test_is_valid_fqcr(self, ref, ref_type, expected, mocker):
        # Mocking the try_parse_fqcr method
        mocker.patch.object(AnsibleCollectionRef, 'try_parse_fqcr', return_value=None)
        
        result = AnsibleCollectionRef.is_valid_fqcr(ref, ref_type)
        assert result == expected
