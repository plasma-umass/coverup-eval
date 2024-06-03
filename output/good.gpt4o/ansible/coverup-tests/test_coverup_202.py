# file lib/ansible/vars/plugins.py:80-95
# lines [80, 82, 83, 85, 86, 87, 88, 89, 91, 93, 95]
# branches ['83->85', '83->95', '85->86', '85->87', '87->88', '87->89', '89->91', '89->93']

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
    sources = [
        None,  # Test the None path
        'host1,host2',  # Test the host list path
        '/non/existent/path',  # Test the non-existent path
        '/tmp/testdir/testfile'  # Test the directory path
    ]

    with mock.patch('os.path.exists', side_effect=lambda x: x != '/non/existent/path'):
        with mock.patch('os.path.isdir', side_effect=lambda x: x == b'/tmp/testdir'):
            result = get_vars_from_inventory_sources(mock_loader, sources, mock_entities, mock_stage)

    assert result == {}
    mock_combine_vars.assert_called()
    mock_get_vars_from_path.assert_called()
