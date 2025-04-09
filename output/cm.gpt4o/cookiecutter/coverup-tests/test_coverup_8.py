# file cookiecutter/replay.py:39-52
# lines [39, 41, 42, 44, 46, 47, 49, 50, 52]
# branches ['41->42', '41->44', '49->50', '49->52']

import pytest
import json
import os
from unittest import mock
from cookiecutter.replay import load

def get_file_name(replay_dir, template_name):
    return os.path.join(replay_dir, f"{template_name}.json")

@pytest.fixture
def mock_replay_file(tmp_path):
    replay_dir = tmp_path / "replay"
    replay_dir.mkdir()
    replay_file = replay_dir / "template.json"
    with replay_file.open("w") as f:
        json.dump({"cookiecutter": {}}, f)
    return replay_dir, replay_file

def test_load_with_invalid_template_name():
    with pytest.raises(TypeError):
        load("some_dir", 123)

def test_load_with_missing_cookiecutter_key(mock_replay_file):
    replay_dir, replay_file = mock_replay_file
    with replay_file.open("w") as f:
        json.dump({}, f)
    with pytest.raises(ValueError):
        load(replay_dir, "template")

def test_load_success(mock_replay_file):
    replay_dir, _ = mock_replay_file
    context = load(replay_dir, "template")
    assert "cookiecutter" in context

def test_load_file_not_found(tmp_path):
    replay_dir = tmp_path / "replay"
    replay_dir.mkdir()
    with pytest.raises(FileNotFoundError):
        load(replay_dir, "non_existent_template")
