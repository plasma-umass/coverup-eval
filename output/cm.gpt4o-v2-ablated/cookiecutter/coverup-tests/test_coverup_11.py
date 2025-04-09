# file: cookiecutter/replay.py:39-52
# asked: {"lines": [41, 42, 44, 46, 47, 49, 50, 52], "branches": [[41, 42], [41, 44], [49, 50], [49, 52]]}
# gained: {"lines": [41, 42, 44, 46, 47, 49, 50, 52], "branches": [[41, 42], [41, 44], [49, 50], [49, 52]]}

import json
import os
import pytest
from unittest.mock import mock_open, patch

# Assuming the function load and get_file_name are imported from cookiecutter/replay.py
from cookiecutter.replay import load, get_file_name

@pytest.fixture
def mock_get_file_name(monkeypatch):
    def mock_get_file_name_func(replay_dir, template_name):
        return os.path.join(replay_dir, f"{template_name}.json")
    monkeypatch.setattr('cookiecutter.replay.get_file_name', mock_get_file_name_func)

def test_load_with_valid_data(mock_get_file_name):
    mock_data = json.dumps({"cookiecutter": {"project_name": "test_project"}})
    with patch("builtins.open", mock_open(read_data=mock_data)):
        context = load("some_dir", "template")
        assert context == {"cookiecutter": {"project_name": "test_project"}}

def test_load_with_invalid_template_name_type(mock_get_file_name):
    with pytest.raises(TypeError, match="Template name is required to be of type str"):
        load("some_dir", 123)

def test_load_with_missing_cookiecutter_key(mock_get_file_name):
    mock_data = json.dumps({"not_cookiecutter": {"project_name": "test_project"}})
    with patch("builtins.open", mock_open(read_data=mock_data)):
        with pytest.raises(ValueError, match="Context is required to contain a cookiecutter key"):
            load("some_dir", "template")
