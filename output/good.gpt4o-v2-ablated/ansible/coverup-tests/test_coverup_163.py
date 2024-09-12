# file: lib/ansible/utils/collection_loader/_collection_finder.py:860-877
# asked: {"lines": [860, 861, 868, 870, 871, 873, 875, 876], "branches": [[870, 871], [870, 873]]}
# gained: {"lines": [860, 861, 868, 870, 871, 873, 875, 876], "branches": [[870, 871], [870, 873]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_text
from keyword import iskeyword
import re

def is_python_identifier(identifier):
    """
    Check if a string is a valid Python identifier
    """
    return re.match(r'^[a-zA-Z_]\w*$', identifier) is not None

@pytest.fixture(autouse=True)
def setup_and_teardown(monkeypatch):
    # Monkeypatch the to_text function to return the input as is
    monkeypatch.setattr('ansible.module_utils._text.to_text', lambda x: x)
    # Monkeypatch the iskeyword function to use the standard library's iskeyword
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.iskeyword', iskeyword)
    # Monkeypatch the is_python_identifier function to use the local implementation
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.is_python_identifier', is_python_identifier)
    yield
    # No specific teardown needed

def test_valid_collection_name():
    assert AnsibleCollectionRef.is_valid_collection_name('namespace.collection') == True

def test_invalid_collection_name_no_dot():
    assert AnsibleCollectionRef.is_valid_collection_name('namespacecollection') == False

def test_invalid_collection_name_multiple_dots():
    assert AnsibleCollectionRef.is_valid_collection_name('namespace.collection.name') == False

def test_invalid_collection_name_keyword():
    assert AnsibleCollectionRef.is_valid_collection_name('for.collection') == False

def test_invalid_collection_name_non_identifier():
    assert AnsibleCollectionRef.is_valid_collection_name('namespace.coll-name') == False

def test_invalid_collection_name_empty_namespace():
    assert AnsibleCollectionRef.is_valid_collection_name('.collection') == False

def test_invalid_collection_name_empty_collection():
    assert AnsibleCollectionRef.is_valid_collection_name('namespace.') == False
