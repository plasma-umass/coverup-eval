# file lib/ansible/utils/collection_loader/_collection_finder.py:659-691
# lines [674]
# branches ['673->674', '676->exit']

import pytest
from unittest import mock
from ansible.utils.collection_loader._collection_finder import _AnsibleInternalRedirectLoader

def _get_collection_metadata(name):
    if name == 'ansible.builtin':
        return {
            'import_redirection': {
                'ansible.some_module': {
                    'redirect': 'ansible.other_module'
                }
            }
        }
    return {}

def _nested_dict_get(d, keys):
    for key in keys:
        d = d.get(key, {})
    return d

@mock.patch('ansible.utils.collection_loader._collection_finder._get_collection_metadata', side_effect=_get_collection_metadata)
@mock.patch('ansible.utils.collection_loader._collection_finder._nested_dict_get', side_effect=_nested_dict_get)
def test_ansible_internal_redirect_loader_no_redirect(mock_get_collection_metadata, mock_nested_dict_get):
    with pytest.raises(ImportError, match='not redirected, go ask path_hook'):
        _AnsibleInternalRedirectLoader('ansible.non_existent_module', [])

@mock.patch('ansible.utils.collection_loader._collection_finder._get_collection_metadata', side_effect=_get_collection_metadata)
@mock.patch('ansible.utils.collection_loader._collection_finder._nested_dict_get', side_effect=_nested_dict_get)
def test_ansible_internal_redirect_loader_with_redirect(mock_get_collection_metadata, mock_nested_dict_get):
    loader = _AnsibleInternalRedirectLoader('ansible.some_module', [])
    assert loader._redirect == 'ansible.other_module'
