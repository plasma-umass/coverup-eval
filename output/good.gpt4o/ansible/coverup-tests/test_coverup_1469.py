# file lib/ansible/utils/collection_loader/_collection_finder.py:422-446
# lines [444]
# branches ['443->444']

import os
import pytest
from unittest import mock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self):
        pass

@pytest.fixture
def mock_os_path(mocker):
    mocker.patch('os.path.isfile', return_value=False)
    mocker.patch('os.path.isdir', return_value=True)
    mocker.patch('os.path.dirname', return_value='/some/dir')

def test_get_data_init_py(mock_os_path):
    loader = MockAnsibleCollectionPkgLoaderBase()
    path = '/some/dir/__init__.py'
    
    result = loader.get_data(path)
    
    assert result == '', "Expected empty string for __init__.py in existing directory"

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
