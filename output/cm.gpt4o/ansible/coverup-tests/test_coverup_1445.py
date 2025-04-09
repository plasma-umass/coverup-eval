# file lib/ansible/playbook/collectionsearch.py:16-31
# lines [25, 29]
# branches ['24->25', '28->29']

import pytest
from unittest import mock
from ansible.playbook.collectionsearch import _ensure_default_collection

@pytest.fixture
def mock_ansible_collection_config(mocker):
    original_default_collection = 'default_collection'
    mocker.patch('ansible.playbook.collectionsearch.AnsibleCollectionConfig', default_collection=original_default_collection)
    yield
    mocker.stopall()

def test_ensure_default_collection_with_default(mock_ansible_collection_config):
    collection_list = _ensure_default_collection()
    assert collection_list == ['default_collection', 'ansible.legacy']

def test_ensure_default_collection_with_custom_list(mock_ansible_collection_config):
    collection_list = _ensure_default_collection(['custom_collection'])
    assert collection_list == ['default_collection', 'custom_collection', 'ansible.legacy']

def test_ensure_default_collection_with_builtin(mock_ansible_collection_config):
    collection_list = _ensure_default_collection(['ansible.builtin'])
    assert collection_list == ['default_collection', 'ansible.builtin']

def test_ensure_default_collection_with_legacy(mock_ansible_collection_config):
    collection_list = _ensure_default_collection(['ansible.legacy'])
    assert collection_list == ['default_collection', 'ansible.legacy']
