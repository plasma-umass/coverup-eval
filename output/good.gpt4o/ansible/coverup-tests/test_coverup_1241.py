# file lib/ansible/vars/plugins.py:80-95
# lines [88]
# branches ['87->88', '89->93']

import os
import pytest
from unittest import mock
from ansible.vars.plugins import get_vars_from_inventory_sources

@pytest.fixture
def mock_loader():
    return mock.Mock()

@pytest.fixture
def mock_entities():
    return mock.Mock()

@pytest.fixture
def mock_stage():
    return mock.Mock()

@pytest.fixture
def mock_combine_vars(mocker):
    return mocker.patch('ansible.vars.plugins.combine_vars', return_value={})

@pytest.fixture
def mock_get_vars_from_path(mocker):
    return mocker.patch('ansible.vars.plugins.get_vars_from_path', return_value={})

def test_get_vars_from_inventory_sources(mock_loader, mock_entities, mock_stage, mock_combine_vars, mock_get_vars_from_path):
    sources = ['host1,host2', '/nonexistent/path', '/tmp/testfile']
    
    with mock.patch('os.path.exists', return_value=False):
        with mock.patch('os.path.isdir', return_value=False):
            result = get_vars_from_inventory_sources(mock_loader, sources, mock_entities, mock_stage)
    
    assert result == {}
    mock_combine_vars.assert_called()
    mock_get_vars_from_path.assert_called()
