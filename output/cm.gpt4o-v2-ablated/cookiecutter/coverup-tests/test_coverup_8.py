# file: cookiecutter/replay.py:19-36
# asked: {"lines": [19, 21, 22, 24, 25, 27, 28, 30, 31, 33, 35, 36], "branches": [[21, 22], [21, 24], [24, 25], [24, 27], [27, 28], [27, 30], [30, 31], [30, 33]]}
# gained: {"lines": [19, 21, 22, 24, 25, 27, 28, 30, 31, 33, 35, 36], "branches": [[21, 22], [21, 24], [24, 25], [24, 27], [27, 28], [27, 30], [30, 31], [30, 33]]}

import pytest
import json
import os

from cookiecutter.replay import dump

def make_sure_path_exists(path):
    """Mock function to simulate path creation."""
    if path == "invalid_path":
        return False
    return True

def get_file_name(replay_dir, template_name):
    """Mock function to simulate file name generation."""
    return os.path.join(replay_dir, f"{template_name}.json")

@pytest.fixture
def mock_make_sure_path_exists(monkeypatch):
    monkeypatch.setattr("cookiecutter.replay.make_sure_path_exists", make_sure_path_exists)

@pytest.fixture
def mock_get_file_name(monkeypatch):
    monkeypatch.setattr("cookiecutter.replay.get_file_name", get_file_name)

@pytest.fixture
def temp_replay_dir(tmp_path):
    return tmp_path / "replay"

def test_dump_success(mock_make_sure_path_exists, mock_get_file_name, temp_replay_dir):
    temp_replay_dir.mkdir()
    template_name = "test_template"
    context = {"cookiecutter": {"project_name": "test_project"}}
    
    dump(temp_replay_dir, template_name, context)
    
    replay_file = temp_replay_dir / f"{template_name}.json"
    assert replay_file.exists()
    
    with open(replay_file, 'r') as f:
        data = json.load(f)
        assert data == context

def test_dump_invalid_replay_dir(mock_make_sure_path_exists, mock_get_file_name):
    with pytest.raises(IOError):
        dump("invalid_path", "test_template", {"cookiecutter": {"project_name": "test_project"}})

def test_dump_invalid_template_name(mock_make_sure_path_exists, mock_get_file_name, temp_replay_dir):
    temp_replay_dir.mkdir()
    with pytest.raises(TypeError):
        dump(temp_replay_dir, 123, {"cookiecutter": {"project_name": "test_project"}})

def test_dump_invalid_context_type(mock_make_sure_path_exists, mock_get_file_name, temp_replay_dir):
    temp_replay_dir.mkdir()
    with pytest.raises(TypeError):
        dump(temp_replay_dir, "test_template", "invalid_context")

def test_dump_missing_cookiecutter_key(mock_make_sure_path_exists, mock_get_file_name, temp_replay_dir):
    temp_replay_dir.mkdir()
    with pytest.raises(ValueError):
        dump(temp_replay_dir, "test_template", {"project_name": "test_project"})
