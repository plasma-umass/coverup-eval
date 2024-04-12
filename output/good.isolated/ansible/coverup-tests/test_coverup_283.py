# file lib/ansible/playbook/collectionsearch.py:16-31
# lines [16, 17, 20, 21, 24, 25, 28, 29, 31]
# branches ['20->21', '20->24', '24->25', '24->28', '28->29', '28->31']

import pytest
from ansible.playbook.collectionsearch import _ensure_default_collection

@pytest.fixture
def ansible_collection_config_mock(mocker):
    mock = mocker.patch('ansible.playbook.collectionsearch.AnsibleCollectionConfig')
    mock.default_collection = 'test.collection'
    return mock

def test_ensure_default_collection_with_default(ansible_collection_config_mock):
    result = _ensure_default_collection()
    assert 'test.collection' in result
    assert 'ansible.legacy' in result

def test_ensure_default_collection_with_existing_list(ansible_collection_config_mock):
    existing_collections = ['my.collection', 'another.collection']
    result = _ensure_default_collection(existing_collections)
    assert 'test.collection' in result
    assert 'ansible.legacy' in result
    assert 'my.collection' in result
    assert 'another.collection' in result

def test_ensure_default_collection_with_builtin(ansible_collection_config_mock):
    existing_collections = ['ansible.builtin']
    result = _ensure_default_collection(existing_collections)
    assert 'test.collection' in result
    assert 'ansible.legacy' not in result
    assert 'ansible.builtin' in result

def test_ensure_default_collection_with_legacy(ansible_collection_config_mock):
    existing_collections = ['ansible.legacy']
    result = _ensure_default_collection(existing_collections)
    assert 'test.collection' in result
    assert 'ansible.legacy' in result
    assert 'ansible.builtin' not in result

def test_ensure_default_collection_with_none_default_collection(ansible_collection_config_mock):
    ansible_collection_config_mock.default_collection = None
    result = _ensure_default_collection()
    assert 'ansible.legacy' not in result  # Corrected assertion
    assert 'test.collection' not in result
    assert result == []  # Added assertion to check for an empty list
