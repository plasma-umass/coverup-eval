# file lib/ansible/utils/collection_loader/_collection_finder.py:860-877
# lines [860, 861, 868, 870, 871, 873, 875, 876]
# branches ['870->871', '870->873']

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_text
from keyword import iskeyword
import re

def is_python_identifier(s):
    return re.match(r'^[a-zA-Z_]\w*$', s) is not None

@pytest.mark.parametrize("collection_name, expected", [
    ("valid_ns.valid_name", True),
    ("invalid_ns.invalid-name", False),
    ("invalid_ns", False),
    ("invalid_ns.invalid.name", False),
    ("invalid_ns.1invalidname", False),
    ("invalid_ns._validname", True),
    ("invalid_ns.validname_", True),
    ("invalid_ns.validname1", True),
    ("invalid_ns.validname$", False),
])
def test_is_valid_collection_name(collection_name, expected, mocker):
    # Mocking to_text to return the input as is
    mocker.patch('ansible.module_utils._text.to_text', return_value=collection_name)
    # Mocking iskeyword to use the actual keyword module's iskeyword function
    mocker.patch('keyword.iskeyword', side_effect=iskeyword)
    # Mocking is_python_identifier to use the local is_python_identifier function
    mocker.patch('ansible.utils.collection_loader._collection_finder.is_python_identifier', side_effect=is_python_identifier)
    
    result = AnsibleCollectionRef.is_valid_collection_name(collection_name)
    assert result == expected
