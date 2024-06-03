# file lib/ansible/utils/collection_loader/_collection_finder.py:880-907
# lines []
# branches ['902->907', '903->907', '905->903']

import os
import sys
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _get_collection_playbook_path

@pytest.fixture
def mock_acr(mocker):
    mock_acr = mocker.patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef')
    mock_acr_instance = mocker.Mock()
    mock_acr_instance.try_parse_fqcr.return_value = mock_acr_instance
    mock_acr_instance.n_python_collection_package_name = 'fake_collection'
    mock_acr_instance.subdirs = ''
    mock_acr_instance.resource = 'fake_playbook'
    mock_acr_instance.collection = 'fake_collection'
    mock_acr.try_parse_fqcr.return_value = mock_acr_instance
    return mock_acr_instance

@pytest.fixture
def mock_import_module(mocker):
    mock_import_module = mocker.patch('ansible.utils.collection_loader._collection_finder.import_module')
    mock_import_module.return_value = MagicMock()
    return mock_import_module

@pytest.fixture
def mock_sys_modules(mocker):
    mock_sys_modules = mocker.patch.dict('sys.modules', {'fake_collection': MagicMock()})
    mock_sys_modules['fake_collection'].__file__ = '/fake/path/__synthetic__'
    return mock_sys_modules

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

def test_get_collection_playbook_path_with_extension(mock_acr, mock_import_module, mock_sys_modules, mock_os_path_exists):
    mock_os_path_exists.side_effect = lambda x: x.endswith(b'.yml')
    playbook = 'fake_collection.fake_playbook'
    result = _get_collection_playbook_path(playbook)
    assert result == ('fake_playbook', '/fake/path/playbooks/fake_playbook.yml', 'fake_collection')

def test_get_collection_playbook_path_without_extension(mock_acr, mock_import_module, mock_sys_modules, mock_os_path_exists):
    mock_os_path_exists.side_effect = lambda x: x.endswith(b'.yml')
    mock_acr.resource = 'fake_playbook_no_ext'
    playbook = 'fake_collection.fake_playbook_no_ext'
    result = _get_collection_playbook_path(playbook)
    assert result == ('fake_playbook_no_ext', '/fake/path/playbooks/fake_playbook_no_ext.yml', 'fake_collection')

def test_get_collection_playbook_path_not_found(mock_acr, mock_import_module, mock_sys_modules, mock_os_path_exists):
    mock_os_path_exists.return_value = False
    mock_acr.resource = 'non_existent_playbook'
    playbook = 'fake_collection.non_existent_playbook'
    result = _get_collection_playbook_path(playbook)
    assert result is None
