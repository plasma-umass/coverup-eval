# file: lib/ansible/utils/collection_loader/_collection_finder.py:914-949
# asked: {"lines": [914, 916, 918, 920, 921, 923, 924, 925, 926, 927, 929, 930, 932, 933, 934, 936, 938, 940, 941, 943, 944, 945, 947, 949], "branches": [[916, 918], [916, 920], [921, 923], [921, 926], [926, 927], [926, 929], [932, 933], [932, 949], [938, 932], [938, 940]]}
# gained: {"lines": [914, 916, 918, 920, 921, 923, 924, 925, 926, 927, 929, 930, 932, 933, 934, 936, 938, 940, 941, 943, 944, 945, 947, 949], "branches": [[916, 918], [916, 920], [921, 923], [921, 926], [926, 927], [926, 929], [932, 933], [932, 949], [938, 940]]}

import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Assuming these are the correct imports based on the code provided
from ansible.utils.collection_loader._collection_finder import _get_collection_resource_path
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

# Mocking the AnsibleCollectionRef and import_module
@pytest.fixture
def mock_ansible_collection_ref(monkeypatch):
    mock_acr = MagicMock()
    mock_acr.try_parse_fqcr = MagicMock(return_value=None)
    mock_acr.return_value = mock_acr
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef', mock_acr)
    return mock_acr

@pytest.fixture
def mock_import_module(monkeypatch):
    mock_import = MagicMock()
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.import_module', mock_import)
    return mock_import

@pytest.fixture
def mock_sys_modules(monkeypatch):
    mock_sys = MagicMock()
    monkeypatch.setattr(sys, 'modules', mock_sys)
    return mock_sys

@pytest.fixture
def mock_os_path(monkeypatch):
    mock_os = MagicMock()
    monkeypatch.setattr(os.path, 'dirname', mock_os.dirname)
    return mock_os

def test_get_collection_resource_path_playbook(mock_ansible_collection_ref):
    with patch('ansible.utils.collection_loader._collection_finder._get_collection_playbook_path', return_value='playbook_path') as mock_playbook_path:
        result = _get_collection_resource_path('test_playbook', 'playbook')
        assert result == 'playbook_path'
        mock_playbook_path.assert_called_once_with('test_playbook')

def test_get_collection_resource_path_fqcr(mock_ansible_collection_ref, mock_import_module, mock_sys_modules, mock_os_path):
    mock_ansible_collection_ref.try_parse_fqcr.return_value = MagicMock(collection='test_collection', subdirs='subdir', resource='resource')
    mock_import_module.return_value = MagicMock()
    mock_sys_modules.__getitem__.return_value.__file__ = '/path/to/module'
    mock_os_path.dirname.return_value = '/path/to'

    result = _get_collection_resource_path('test_fqcr', 'module')
    assert result == ('resource', '/path/to', 'test_collection')

def test_get_collection_resource_path_no_collection_list(mock_ansible_collection_ref):
    result = _get_collection_resource_path('test_name', 'module')
    assert result is None

def test_get_collection_resource_path_unqualified(mock_ansible_collection_ref, mock_import_module, mock_sys_modules, mock_os_path):
    mock_import_module.return_value = MagicMock()
    mock_sys_modules.__getitem__.return_value.__file__ = '/path/to/module'
    mock_os_path.dirname.return_value = '/path/to'

    result = _get_collection_resource_path('test_name', 'module', ['test_collection'])
    assert result == ('test_name', '/path/to', 'test_collection')

def test_get_collection_resource_path_import_error(mock_ansible_collection_ref, mock_import_module):
    mock_import_module.side_effect = ModuleNotFoundError
    result = _get_collection_resource_path('test_name', 'module', ['test_collection'])
    assert result is None

def test_get_collection_resource_path_io_error(mock_ansible_collection_ref, mock_import_module):
    mock_import_module.side_effect = IOError
    result = _get_collection_resource_path('test_name', 'module', ['test_collection'])
    assert result is None

def test_get_collection_resource_path_generic_exception(mock_ansible_collection_ref, mock_import_module):
    mock_import_module.side_effect = Exception
    result = _get_collection_resource_path('test_name', 'module', ['test_collection'])
    assert result is None
