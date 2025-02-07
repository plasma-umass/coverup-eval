# file: lib/ansible/utils/collection_loader/_collection_finder.py:569-585
# asked: {"lines": [569, 585], "branches": []}
# gained: {"lines": [569], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoader

class MockAnsibleCollectionPkgLoader(_AnsibleCollectionPkgLoader):
    def __init__(self, split_name):
        self._split_name = split_name

    def _canonicalize_meta(self, meta_dict):
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
def loader():
    return MockAnsibleCollectionPkgLoader(split_name=['namespace', 'collection', 'plugin'])

def test_canonicalize_meta_empty_dict(loader):
    meta_dict = {}
    result = loader._canonicalize_meta(meta_dict)
    assert result == {}

def test_canonicalize_meta_with_data(loader):
    meta_dict = {
        'plugin_routing': {
            'type1': {
                'plugin1': {
                    'redirect': '..redirect_target'
                }
            }
        }
    }
    result = loader._canonicalize_meta(meta_dict)
    assert result == {
        'plugin_routing': {
            'type1': {
                'plugin1': {
                    'redirect': 'redirect_target'
                }
            }
        }
    }
