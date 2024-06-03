# file lib/ansible/utils/collection_loader/_collection_finder.py:914-949
# lines [914, 916, 918, 920, 921, 923, 924, 925, 926, 927, 929, 930, 932, 933, 934, 936, 938, 940, 941, 943, 944, 945, 947, 949]
# branches ['916->918', '916->920', '921->923', '921->926', '926->927', '926->929', '932->933', '932->949', '938->932', '938->940']

import pytest
from unittest import mock
from ansible.utils.collection_loader._collection_finder import _get_collection_resource_path, AnsibleCollectionRef
import sys
import os

@pytest.fixture
def mock_import_module(mocker):
    return mocker.patch('ansible.utils.collection_loader._collection_finder.import_module')

@pytest.fixture
def mock_to_bytes(mocker):
    return mocker.patch('ansible.utils.collection_loader._collection_finder.to_bytes', side_effect=lambda x, errors: x.encode())

@pytest.fixture
def mock_to_text(mocker):
    return mocker.patch('ansible.utils.collection_loader._collection_finder.to_text', side_effect=lambda x, errors: x.decode())

@pytest.fixture
def mock_sys_modules(mocker):
    mocker.patch.dict(sys.modules, {'mocked_package': mock.Mock(__file__='/mocked/path/__init__.py')})

class MockAnsibleCollectionRef:
    def __init__(self, collection_name, subdirs, resource, ref_type):
        self.collection = collection_name
        self.subdirs = subdirs
        self.resource = resource
        self.ref_type = ref_type
        self.n_python_package_name = 'mocked_package'

    @staticmethod
    def try_parse_fqcr(name, ref_type):
        if name == 'test_collection.resource':
            return MockAnsibleCollectionRef('test_collection', 'subdir', 'resource', 'module')
        return None

def test_get_collection_resource_path_playbook(mocker):
    mock_get_collection_playbook_path = mocker.patch('ansible.utils.collection_loader._collection_finder._get_collection_playbook_path', return_value='playbook_path')
    result = _get_collection_resource_path('test_playbook', 'playbook')
    assert result == 'playbook_path'
    mock_get_collection_playbook_path.assert_called_once_with('test_playbook')

def test_get_collection_resource_path_fqcr(mock_import_module, mock_to_bytes, mock_to_text, mock_sys_modules, mocker):
    mock_import_module.return_value = mock.Mock()
    mocker.patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef', MockAnsibleCollectionRef)
    
    result = _get_collection_resource_path('test_collection.resource', 'module')
    assert result == ('resource', '/mocked/path', 'test_collection')

def test_get_collection_resource_path_no_collection_list():
    result = _get_collection_resource_path('test_resource', 'module')
    assert result is None

def test_get_collection_resource_path_unqualified(mock_import_module, mock_to_bytes, mock_to_text, mock_sys_modules, mocker):
    mock_import_module.return_value = mock.Mock()
    mocker.patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef', MockAnsibleCollectionRef)
    
    result = _get_collection_resource_path('test_resource', 'module', collection_list=['test_collection'])
    assert result == ('test_resource', '/mocked/path', 'test_collection')

def test_get_collection_resource_path_import_error(mock_import_module):
    mock_import_module.side_effect = ModuleNotFoundError
    
    result = _get_collection_resource_path('test_resource', 'module', collection_list=['test_collection'])
    assert result is None

def test_get_collection_resource_path_generic_exception(mock_import_module):
    mock_import_module.side_effect = Exception
    
    result = _get_collection_resource_path('test_resource', 'module', collection_list=['test_collection'])
    assert result is None
