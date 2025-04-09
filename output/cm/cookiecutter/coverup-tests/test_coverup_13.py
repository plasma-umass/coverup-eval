# file cookiecutter/replay.py:39-52
# lines [39, 41, 42, 44, 46, 47, 49, 50, 52]
# branches ['41->42', '41->44', '49->50', '49->52']

import json
import os
import pytest
from cookiecutter.replay import load

@pytest.fixture
def mock_replay_dir(tmp_path):
    replay_dir = tmp_path / "replay"
    replay_dir.mkdir()
    return replay_dir

@pytest.fixture
def mock_template_name():
    return "test_template"

@pytest.fixture
def mock_replay_file(mock_replay_dir, mock_template_name):
    replay_file = mock_replay_dir / f"{mock_template_name}.json"
    return replay_file

def test_load_with_invalid_template_name(mock_replay_dir):
    with pytest.raises(TypeError):
        load(mock_replay_dir, 123)  # Non-string template_name should raise TypeError

def test_load_with_missing_cookiecutter_key(mock_replay_dir, mock_template_name, mock_replay_file):
    # Create a replay file without 'cookiecutter' key
    data = {"not_cookiecutter": {}}
    with open(mock_replay_file, 'w') as f:
        json.dump(data, f)

    with pytest.raises(ValueError):
        load(mock_replay_dir, mock_template_name)

def test_load_with_valid_context(mock_replay_dir, mock_template_name, mock_replay_file):
    # Create a valid replay file with 'cookiecutter' key
    expected_context = {"cookiecutter": {"project_slug": "test_project"}}
    with open(mock_replay_file, 'w') as f:
        json.dump(expected_context, f)

    context = load(mock_replay_dir, mock_template_name)
    assert context == expected_context, "The context loaded from the replay file should match the expected context"
