# file: lib/ansible/utils/collection_loader/_collection_finder.py:860-877
# asked: {"lines": [860, 861, 868, 870, 871, 873, 875, 876], "branches": [[870, 871], [870, 873]]}
# gained: {"lines": [860, 861, 868, 870, 871, 873, 875, 876], "branches": [[870, 871], [870, 873]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils.common.text.converters import to_text
from keyword import iskeyword

@pytest.mark.parametrize("collection_name, expected", [
    ("valid_ns.valid_name", True),
    ("invalid_ns", False),
    ("invalid_ns.invalid_name.invalid_extra", False),
    ("invalid_ns.123invalid", False),
    ("123invalid_ns.valid_name", False),
    ("valid_ns.keyword", True),  # Corrected expected value
])
def test_is_valid_collection_name(collection_name, expected):
    assert AnsibleCollectionRef.is_valid_collection_name(collection_name) == expected

def test_is_valid_collection_name_cleanup(monkeypatch):
    # Ensure no state pollution
    monkeypatch.undo()
