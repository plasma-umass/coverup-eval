# file: cookiecutter/replay.py:39-52
# asked: {"lines": [39, 41, 42, 44, 46, 47, 49, 50, 52], "branches": [[41, 42], [41, 44], [49, 50], [49, 52]]}
# gained: {"lines": [39, 41, 42, 44, 46, 47, 49, 50, 52], "branches": [[41, 42], [41, 44], [49, 50], [49, 52]]}

import pytest
import json
import os
from unittest.mock import mock_open, patch
from cookiecutter.replay import load, get_file_name

def test_load_with_valid_data(monkeypatch):
    replay_dir = "test_dir"
    template_name = "test_template"
    replay_file = os.path.join(replay_dir, f"{template_name}.json")
    mock_data = {"cookiecutter": {"key": "value"}}
    
    monkeypatch.setattr("builtins.open", mock_open(read_data=json.dumps(mock_data)))
    monkeypatch.setattr("os.path.join", lambda *args: replay_file)
    
    result = load(replay_dir, template_name)
    
    assert result == mock_data

def test_load_with_invalid_template_name_type():
    with pytest.raises(TypeError):
        load("test_dir", 123)

def test_load_with_missing_cookiecutter_key(monkeypatch):
    replay_dir = "test_dir"
    template_name = "test_template"
    replay_file = os.path.join(replay_dir, f"{template_name}.json")
    mock_data = {"not_cookiecutter": {"key": "value"}}
    
    monkeypatch.setattr("builtins.open", mock_open(read_data=json.dumps(mock_data)))
    monkeypatch.setattr("os.path.join", lambda *args: replay_file)
    
    with pytest.raises(ValueError):
        load(replay_dir, template_name)

def test_get_file_name_with_json_suffix():
    replay_dir = "test_dir"
    template_name = "test_template.json"
    expected = os.path.join(replay_dir, template_name)
    
    result = get_file_name(replay_dir, template_name)
    
    assert result == expected

def test_get_file_name_without_json_suffix():
    replay_dir = "test_dir"
    template_name = "test_template"
    expected = os.path.join(replay_dir, f"{template_name}.json")
    
    result = get_file_name(replay_dir, template_name)
    
    assert result == expected
