# file lib/ansible/utils/collection_loader/_collection_finder.py:860-877
# lines [860, 861, 868, 870, 871, 873, 875, 876]
# branches ['870->871', '870->873']

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from keyword import iskeyword
from ansible.module_utils._text import to_text

# Mocking the is_python_identifier function
def mock_is_python_identifier(name):
    return name.isidentifier()

@pytest.fixture
def mock_is_python_identifier_fixture(mocker):
    mocker.patch('ansible.utils.collection_loader._collection_finder.is_python_identifier', side_effect=mock_is_python_identifier)

def test_ansible_collection_ref_valid_name(mock_is_python_identifier_fixture):
    valid_collection_name = "namespace.collection_name"
    assert AnsibleCollectionRef.is_valid_collection_name(valid_collection_name) is True

def test_ansible_collection_ref_invalid_name_no_dot(mock_is_python_identifier_fixture):
    invalid_collection_name = "invalidcollectionname"
    assert AnsibleCollectionRef.is_valid_collection_name(invalid_collection_name) is False

def test_ansible_collection_ref_invalid_name_two_dots(mock_is_python_identifier_fixture):
    invalid_collection_name = "namespace..collection_name"
    assert AnsibleCollectionRef.is_valid_collection_name(invalid_collection_name) is False

def test_ansible_collection_ref_invalid_name_keyword(mock_is_python_identifier_fixture):
    invalid_collection_name = "namespace.for"
    assert AnsibleCollectionRef.is_valid_collection_name(invalid_collection_name) is False

def test_ansible_collection_ref_invalid_name_non_identifier(mock_is_python_identifier_fixture):
    invalid_collection_name = "namespace.123collection"
    assert AnsibleCollectionRef.is_valid_collection_name(invalid_collection_name) is False
