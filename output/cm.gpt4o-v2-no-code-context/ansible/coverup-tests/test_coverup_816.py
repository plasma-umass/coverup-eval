# file: lib/ansible/utils/collection_loader/_collection_finder.py:569-585
# asked: {"lines": [569, 585], "branches": []}
# gained: {"lines": [569], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoader

class MockAnsibleCollectionPkgLoader(_AnsibleCollectionPkgLoader):
    def __init__(self, split_name):
        self._split_name = split_name
        self._subpackage_search_paths = []

    def _canonicalize_meta(self, meta_dict):
        if not meta_dict:
            return {}
        
        ns_name = '.'.join(self._split_name[0:2])
        collection_name = '.'.join(self._split_name[0:3])
        
        for routing_type, routing_type_dict in meta_dict.get('plugin_routing', {}).items():
            for plugin_key, plugin_dict in routing_type_dict.items():
                redirect = plugin_dict.get('redirect', '')
                if redirect.startswith('..'):
                    redirect = redirect[2:]
                plugin_dict['redirect'] = redirect
        
        return meta_dict

@pytest.fixture
def mock_loader():
    return MockAnsibleCollectionPkgLoader(split_name=['namespace', 'collection', 'plugin'])

def test_canonicalize_meta_empty_dict(mock_loader):
    meta_dict = {}
    result = mock_loader._canonicalize_meta(meta_dict)
    assert result == {}

def test_canonicalize_meta_with_redirect(mock_loader):
    meta_dict = {
        'plugin_routing': {
            'type1': {
                'plugin1': {
                    'redirect': '..redirect_target'
                }
            }
        }
    }
    result = mock_loader._canonicalize_meta(meta_dict)
    assert result['plugin_routing']['type1']['plugin1']['redirect'] == 'redirect_target'

def test_canonicalize_meta_with_current_collection_redirect(mock_loader):
    meta_dict = {
        'plugin_routing': {
            'type1': {
                'plugin1': {
                    'redirect': '.redirect_target'
                }
            }
        }
    }
    result = mock_loader._canonicalize_meta(meta_dict)
    assert result['plugin_routing']['type1']['plugin1']['redirect'] == '.redirect_target'

def test_canonicalize_meta_no_redirect(mock_loader):
    meta_dict = {
        'plugin_routing': {
            'type1': {
                'plugin1': {
                    'redirect': 'redirect_target'
                }
            }
        }
    }
    result = mock_loader._canonicalize_meta(meta_dict)
    assert result['plugin_routing']['type1']['plugin1']['redirect'] == 'redirect_target'
