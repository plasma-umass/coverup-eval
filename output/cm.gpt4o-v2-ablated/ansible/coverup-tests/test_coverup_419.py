# file: lib/ansible/parsing/dataloader.py:82-106
# asked: {"lines": [85, 86, 90, 91, 94, 96, 97, 100, 102, 103, 106], "branches": [[90, 91], [90, 94], [102, 103], [102, 106]]}
# gained: {"lines": [85, 86, 90, 91, 94, 96, 97, 100, 102, 103, 106], "branches": [[90, 91], [90, 94], [102, 103], [102, 106]]}

import pytest
import json
import yaml
import os
from unittest.mock import MagicMock, patch
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._FILE_CACHE = {}
    return loader

@pytest.fixture
def mock_file(tmp_path):
    file_path = tmp_path / "test_file"
    return file_path

def test_load_from_file_cache(dataloader, mock_file, monkeypatch):
    dataloader._FILE_CACHE[str(mock_file)] = {"cached": "data"}
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: str(mock_file))
    result = dataloader.load_from_file(str(mock_file))
    assert result == {"cached": "data"}

def test_load_from_file_no_cache(dataloader, mock_file, monkeypatch):
    file_content = json.dumps({"key": "value"})
    mock_file.write_text(file_content)
    
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: str(mock_file))
    monkeypatch.setattr(dataloader, '_get_file_contents', lambda x: (file_content.encode(), True))
    monkeypatch.setattr(dataloader, 'load', lambda data, file_name, show_content, json_only: json.loads(data))
    
    result = dataloader.load_from_file(str(mock_file))
    assert result == {"key": "value"}
    assert dataloader._FILE_CACHE[str(mock_file)] == {"key": "value"}

def test_load_from_file_unsafe(dataloader, mock_file, monkeypatch):
    file_content = json.dumps({"key": "value"})
    mock_file.write_text(file_content)
    
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: str(mock_file))
    monkeypatch.setattr(dataloader, '_get_file_contents', lambda x: (file_content.encode(), True))
    monkeypatch.setattr(dataloader, 'load', lambda data, file_name, show_content, json_only: json.loads(data))
    
    result = dataloader.load_from_file(str(mock_file), unsafe=True)
    assert result == {"key": "value"}

def test_load_from_file_yaml(dataloader, mock_file, monkeypatch):
    file_content = yaml.dump({"key": "value"})
    mock_file.write_text(file_content)
    
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: str(mock_file))
    monkeypatch.setattr(dataloader, '_get_file_contents', lambda x: (file_content.encode(), True))
    monkeypatch.setattr(dataloader, 'load', lambda data, file_name, show_content, json_only: yaml.safe_load(data))
    
    result = dataloader.load_from_file(str(mock_file))
    assert result == {"key": "value"}
    assert dataloader._FILE_CACHE[str(mock_file)] == {"key": "value"}

def test_load_from_file_json_only(dataloader, mock_file, monkeypatch):
    file_content = json.dumps({"key": "value"})
    mock_file.write_text(file_content)
    
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: str(mock_file))
    monkeypatch.setattr(dataloader, '_get_file_contents', lambda x: (file_content.encode(), True))
    monkeypatch.setattr(dataloader, 'load', lambda data, file_name, show_content, json_only: json.loads(data) if json_only else yaml.safe_load(data))
    
    result = dataloader.load_from_file(str(mock_file), json_only=True)
    assert result == {"key": "value"}
    assert dataloader._FILE_CACHE[str(mock_file)] == {"key": "value"}
