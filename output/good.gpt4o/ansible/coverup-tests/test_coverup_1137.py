# file lib/ansible/utils/collection_loader/_collection_finder.py:880-907
# lines [887, 889, 901, 907]
# branches ['883->907', '891->907', '894->899', '900->901', '902->907', '903->907', '905->903']

import os
import sys
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _get_collection_playbook_path, AnsibleCollectionRef

@pytest.fixture
def mock_ansible_collection_ref(mocker):
    mock_acr = mocker.patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef')
    mock_acr.try_parse_fqcr.return_value = MagicMock(
        n_python_collection_package_name='mock_package',
        subdirs='subdir1.subdir2',
        resource='playbook_name',
        collection='mock_collection'
    )
    return mock_acr

@pytest.fixture
def mock_import_module(mocker):
    return mocker.patch('ansible.utils.collection_loader._collection_finder.import_module')

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

@pytest.fixture
def mock_sys_modules(mocker):
    mock_sys_modules = mocker.patch.dict('sys.modules', {
        'mock_package': MagicMock(__file__='mock_path/__synthetic__')
    })
    return mock_sys_modules

def test_get_collection_playbook_path_success(mock_ansible_collection_ref, mock_import_module, mock_os_path_exists, mock_sys_modules):
    mock_os_path_exists.side_effect = [False, True]  # First call for the initial path, second for the path with extension

    result = _get_collection_playbook_path('mock_playbook')

    assert result == ('playbook_name', 'mock_path/playbooks/subdir1/subdir2/playbook_name.yml', 'mock_collection')

def test_get_collection_playbook_path_no_acr():
    result = _get_collection_playbook_path('invalid_playbook')
    assert result is None

def test_get_collection_playbook_path_import_error(mock_ansible_collection_ref, mock_import_module, mock_os_path_exists, mock_sys_modules):
    mock_import_module.side_effect = ModuleNotFoundError

    result = _get_collection_playbook_path('mock_playbook')

    assert result is None

def test_get_collection_playbook_path_no_subdirs(mock_ansible_collection_ref, mock_import_module, mock_os_path_exists, mock_sys_modules):
    mock_ansible_collection_ref.try_parse_fqcr.return_value.subdirs = ''
    mock_os_path_exists.side_effect = [True]

    result = _get_collection_playbook_path('mock_playbook')

    assert result == ('playbook_name', 'mock_path/playbooks/playbook_name', 'mock_collection')

def test_get_collection_playbook_path_no_extension(mock_ansible_collection_ref, mock_import_module, mock_os_path_exists, mock_sys_modules):
    mock_ansible_collection_ref.try_parse_fqcr.return_value.resource = 'playbook_name'
    mock_os_path_exists.side_effect = [False, True]

    result = _get_collection_playbook_path('mock_playbook')

    assert result == ('playbook_name', 'mock_path/playbooks/subdir1/subdir2/playbook_name.yml', 'mock_collection')
