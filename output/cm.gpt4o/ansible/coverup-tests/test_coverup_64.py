# file lib/ansible/utils/collection_loader/_collection_finder.py:880-907
# lines [880, 882, 883, 884, 886, 887, 889, 891, 892, 894, 895, 896, 897, 899, 900, 901, 902, 903, 904, 905, 906, 907]
# branches ['883->884', '883->907', '891->892', '891->907', '894->895', '894->899', '900->901', '900->902', '902->903', '902->907', '903->904', '903->907', '905->903', '905->906']

import os
import sys
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _get_collection_playbook_path
from ansible.utils.collection_loader import AnsibleCollectionRef

@pytest.fixture
def mock_ansible_collection_ref(mocker):
    mock_acr = mocker.patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef')
    mock_acr.try_parse_fqcr.return_value = MagicMock(
        n_python_collection_package_name='test_collection',
        subdirs='subdir1.subdir2',
        resource='test_playbook',
        collection='test_collection'
    )
    return mock_acr

@pytest.fixture
def mock_import_module(mocker):
    return mocker.patch('ansible.utils.collection_loader._collection_finder.import_module')

@pytest.fixture
def mock_sys_modules(mocker):
    mock_sys_modules = mocker.patch.dict('sys.modules', {
        'test_collection': MagicMock(__file__='__synthetic__')
    })
    return mock_sys_modules

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

def test_get_collection_playbook_path(mock_ansible_collection_ref, mock_import_module, mock_sys_modules, mock_os_path_exists):
    mock_os_path_exists.side_effect = [False, True]  # First call returns False, second call returns True

    result = _get_collection_playbook_path('test_collection::test_playbook')

    assert result == ('test_playbook', os.path.join('playbooks', 'subdir1', 'subdir2', 'test_playbook.yml'), 'test_collection')

    mock_ansible_collection_ref.try_parse_fqcr.assert_called_once_with('test_collection::test_playbook', 'playbook')
    mock_import_module.assert_called_once_with('test_collection')
    mock_os_path_exists.assert_any_call(b'playbooks/subdir1/subdir2/test_playbook')
    mock_os_path_exists.assert_any_call(b'playbooks/subdir1/subdir2/test_playbook.yml')
