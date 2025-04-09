# file: lib/ansible/utils/collection_loader/_collection_finder.py:844-858
# asked: {"lines": [858], "branches": [[855, 858]]}
# gained: {"lines": [858], "branches": [[855, 858]]}

import pytest
import re
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

# Mocking the to_text function and other dependencies
def to_text(data):
    if isinstance(data, bytes):
        return data.decode('utf-8')
    return str(data)

# Mocking the VALID_FQCR_RE and try_parse_fqcr for the purpose of testing
AnsibleCollectionRef.VALID_FQCR_RE = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*$')

def mock_try_parse_fqcr(ref, ref_type):
    # Mock behavior for try_parse_fqcr
    if ref_type == 'module' and ref.endswith('.py'):
        return True
    return False

AnsibleCollectionRef.try_parse_fqcr = staticmethod(mock_try_parse_fqcr)

@pytest.mark.parametrize("ref, ref_type, expected", [
    ("namespace.collection.module", None, True),
    ("namespace.collection.module", "module", False),
    ("namespace.collection.module.py", "module", True),
    ("namespace.collection.module", "role", False),
])
def test_is_valid_fqcr(monkeypatch, ref, ref_type, expected):
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.to_text', to_text)
    result = AnsibleCollectionRef.is_valid_fqcr(ref, ref_type)
    assert result == expected
