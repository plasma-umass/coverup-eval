# file: lib/ansible/vars/plugins.py:80-95
# asked: {"lines": [80, 82, 83, 85, 86, 87, 88, 89, 91, 93, 95], "branches": [[83, 85], [83, 95], [85, 86], [85, 87], [87, 88], [87, 89], [89, 91], [89, 93]]}
# gained: {"lines": [80, 82, 83, 85, 86, 87, 88, 89, 91, 93, 95], "branches": [[83, 85], [83, 95], [85, 86], [85, 87], [87, 88], [87, 89], [89, 91], [89, 93]]}

import os
import pytest
from unittest.mock import Mock, patch
from ansible.module_utils._text import to_bytes
from ansible.utils.vars import combine_vars
from ansible.vars.plugins import get_vars_from_inventory_sources

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_entities():
    return Mock()

@pytest.fixture
def mock_stage():
    return Mock()

@pytest.fixture
def mock_get_vars_from_path():
    with patch('ansible.vars.plugins.get_vars_from_path', return_value={}) as mock:
        yield mock

def test_get_vars_from_inventory_sources_none_path(mock_loader, mock_entities, mock_stage, mock_get_vars_from_path):
    sources = [None]
    result = get_vars_from_inventory_sources(mock_loader, sources, mock_entities, mock_stage)
    assert result == {}
    mock_get_vars_from_path.assert_not_called()

def test_get_vars_from_inventory_sources_comma_in_path(mock_loader, mock_entities, mock_stage, mock_get_vars_from_path):
    sources = ["host1,host2"]
    with patch('os.path.exists', return_value=False):
        result = get_vars_from_inventory_sources(mock_loader, sources, mock_entities, mock_stage)
    assert result == {}
    mock_get_vars_from_path.assert_not_called()

def test_get_vars_from_inventory_sources_not_directory(mock_loader, mock_entities, mock_stage, mock_get_vars_from_path):
    sources = ["/path/to/file"]
    with patch('os.path.exists', return_value=True), patch('os.path.isdir', return_value=False):
        result = get_vars_from_inventory_sources(mock_loader, sources, mock_entities, mock_stage)
    mock_get_vars_from_path.assert_called_once()
    assert result == {}

def test_get_vars_from_inventory_sources_directory(mock_loader, mock_entities, mock_stage, mock_get_vars_from_path):
    sources = ["/path/to/directory"]
    with patch('os.path.exists', return_value=True), patch('os.path.isdir', return_value=True):
        result = get_vars_from_inventory_sources(mock_loader, sources, mock_entities, mock_stage)
    mock_get_vars_from_path.assert_called_once()
    assert result == {}
