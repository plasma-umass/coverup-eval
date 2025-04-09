# file: lib/ansible/utils/collection_loader/_collection_finder.py:534-567
# asked: {"lines": [536, 552, 553, 554, 555, 557, 562, 563], "branches": [[535, 536], [545, 552], [553, 554], [553, 557], [559, 565]]}
# gained: {"lines": [536, 552, 553, 554, 555, 557, 562, 563], "branches": [[535, 536], [545, 552], [553, 554], [553, 557], [559, 565]]}

import pytest
import os
from unittest.mock import MagicMock, patch, mock_open

# Assuming the module and classes are imported correctly
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoader

@pytest.fixture
def mock_loader():
    class MockLoader(_AnsibleCollectionPkgLoader):
        def __init__(self):
            self._split_name = ['ansible', 'test_collection']
            self.__path__ = ['/fake/path']
            self._subpackage_search_paths = []
            self._source_code_path = '/fake/source_code_path'
    return MockLoader()

def test_load_module_meta_yml_not_set(mock_loader):
    with patch('ansible.utils.collection_loader._collection_finder._meta_yml_to_dict', None):
        with pytest.raises(ValueError, match='ansible.utils.collection_loader._meta_yml_to_dict is not set'):
            mock_loader.load_module('ansible.test_collection')

def test_load_module_no_runtime_yml(mock_loader, monkeypatch):
    monkeypatch.setattr(os.path, 'isfile', lambda x: False)
    monkeypatch.setattr('builtins.open', mock_open(read_data=''))
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._meta_yml_to_dict', lambda x, y: {})
    mock_module = MagicMock()
    mock_module.__path__ = ['/fake/path']
    mock_module.__file__ = '/fake/path/module.py'
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._AnsibleCollectionPkgLoaderBase.load_module', lambda self, fullname: mock_module)

    module = mock_loader.load_module('ansible.test_collection')
    assert module._collection_meta == {}

def test_load_module_with_runtime_yml(mock_loader, monkeypatch):
    monkeypatch.setattr(os.path, 'isfile', lambda x: True)
    monkeypatch.setattr('builtins.open', mock_open(read_data='routing_data'))
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._meta_yml_to_dict', lambda x, y: {'key': 'value'})
    mock_module = MagicMock()
    mock_module.__path__ = ['/fake/path']
    mock_module.__file__ = '/fake/path/module.py'
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._AnsibleCollectionPkgLoaderBase.load_module', lambda self, fullname: mock_module)

    module = mock_loader.load_module('ansible.test_collection')
    assert module._collection_meta == {'key': 'value'}

def test_load_module_runtime_yml_exception(mock_loader, monkeypatch):
    monkeypatch.setattr(os.path, 'isfile', lambda x: True)
    monkeypatch.setattr('builtins.open', mock_open(read_data='routing_data'))
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._meta_yml_to_dict', lambda x, y: (_ for _ in ()).throw(Exception('test exception')))
    mock_module = MagicMock()
    mock_module.__path__ = ['/fake/path']
    mock_module.__file__ = '/fake/path/module.py'
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._AnsibleCollectionPkgLoaderBase.load_module', lambda self, fullname: mock_module)

    with pytest.raises(ValueError, match='error parsing collection metadata: test exception'):
        mock_loader.load_module('ansible.test_collection')

def test_load_module_fire_event(mock_loader, monkeypatch):
    monkeypatch.setattr(os.path, 'isfile', lambda x: False)
    monkeypatch.setattr('builtins.open', mock_open(read_data=''))
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._meta_yml_to_dict', lambda x, y: {})
    mock_module = MagicMock()
    mock_module.__path__ = ['/fake/path']
    mock_module.__file__ = '/fake/path/module.py'
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._AnsibleCollectionPkgLoaderBase.load_module', lambda self, fullname: mock_module)
    mock_fire = MagicMock()
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.AnsibleCollectionConfig.on_collection_load.fire', mock_fire)

    module = mock_loader.load_module('ansible.test_collection')
    mock_fire.assert_called_once_with(collection_name='test_collection', collection_path='/fake/path')
