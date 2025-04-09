# file: lib/ansible/vars/plugins.py:80-95
# asked: {"lines": [80, 82, 83, 85, 86, 87, 88, 89, 91, 93, 95], "branches": [[83, 85], [83, 95], [85, 86], [85, 87], [87, 88], [87, 89], [89, 91], [89, 93]]}
# gained: {"lines": [80, 82, 83, 85, 86, 87, 88, 89, 91, 93, 95], "branches": [[83, 85], [83, 95], [85, 86], [85, 87], [87, 88], [87, 89], [89, 91], [89, 93]]}

import os
import pytest
from unittest.mock import MagicMock, patch

# Assuming the function to be tested is imported from the module
from ansible.vars.plugins import get_vars_from_inventory_sources

def test_get_vars_from_inventory_sources_with_none_path():
    loader = MagicMock()
    sources = [None]
    entities = MagicMock()
    stage = MagicMock()

    result = get_vars_from_inventory_sources(loader, sources, entities, stage)
    assert result == {}

def test_get_vars_from_inventory_sources_with_comma_in_path(monkeypatch):
    loader = MagicMock()
    sources = ["host1,host2"]
    entities = MagicMock()
    stage = MagicMock()

    monkeypatch.setattr(os.path, 'exists', lambda x: False)

    result = get_vars_from_inventory_sources(loader, sources, entities, stage)
    assert result == {}

def test_get_vars_from_inventory_sources_with_non_existent_directory(monkeypatch):
    loader = MagicMock()
    sources = ["/non/existent/path"]
    entities = MagicMock()
    stage = MagicMock()

    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr(os.path, 'isdir', lambda x: False)
    monkeypatch.setattr(os.path, 'dirname', lambda x: "/non/existent")

    with patch('ansible.vars.plugins.get_vars_from_path', return_value={}):
        result = get_vars_from_inventory_sources(loader, sources, entities, stage)
        assert result == {}

def test_get_vars_from_inventory_sources_with_valid_directory(monkeypatch):
    loader = MagicMock()
    sources = ["/valid/path"]
    entities = MagicMock()
    stage = MagicMock()

    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr(os.path, 'isdir', lambda x: True)

    with patch('ansible.vars.plugins.get_vars_from_path', return_value={"key": "value"}):
        result = get_vars_from_inventory_sources(loader, sources, entities, stage)
        assert result == {"key": "value"}

def test_get_vars_from_inventory_sources_combined_vars(monkeypatch):
    loader = MagicMock()
    sources = ["/valid/path1", "/valid/path2"]
    entities = MagicMock()
    stage = MagicMock()

    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr(os.path, 'isdir', lambda x: True)

    def mock_get_vars_from_path(loader, path, entities, stage):
        if path == "/valid/path1":
            return {"key1": "value1"}
        elif path == "/valid/path2":
            return {"key2": "value2"}
        return {}

    with patch('ansible.vars.plugins.get_vars_from_path', side_effect=mock_get_vars_from_path):
        with patch('ansible.vars.plugins.combine_vars', lambda x, y: {**x, **y}):
            result = get_vars_from_inventory_sources(loader, sources, entities, stage)
            assert result == {"key1": "value1", "key2": "value2"}
