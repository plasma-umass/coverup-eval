# file: lib/ansible/utils/collection_loader/_collection_finder.py:860-877
# asked: {"lines": [871], "branches": [[870, 871]]}
# gained: {"lines": [871], "branches": [[870, 871]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_text
from keyword import iskeyword
import re

def is_python_identifier(identifier):
    """
    Check if a string is a valid Python identifier.
    """
    return re.match(r'^[a-zA-Z_]\w*$', identifier) is not None

@pytest.mark.parametrize("collection_name, expected", [
    ("valid_ns.valid_name", True),
    ("invalid_ns", False),  # This should trigger line 871
    ("invalid_ns.invalid_name.invalid_extra", False),  # This should also trigger line 871
    ("invalid_ns.1nvalid_name", False),
    ("invalid_ns.invalid-name", False),
    ("invalid_ns.invalid name", False),
    ("invalid_ns.invalid_name!", False),
])
def test_is_valid_collection_name(collection_name, expected):
    result = AnsibleCollectionRef.is_valid_collection_name(collection_name)
    assert result == expected
