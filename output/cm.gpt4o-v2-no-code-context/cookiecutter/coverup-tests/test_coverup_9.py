# file: cookiecutter/replay.py:39-52
# asked: {"lines": [39, 41, 42, 44, 46, 47, 49, 50, 52], "branches": [[41, 42], [41, 44], [49, 50], [49, 52]]}
# gained: {"lines": [39, 41, 42, 44, 46, 47, 49, 50, 52], "branches": [[41, 42], [41, 44], [49, 50], [49, 52]]}

import json
import os
import pytest
from unittest import mock
from cookiecutter.replay import load

def get_file_name(replay_dir, template_name):
    return os.path.join(replay_dir, f"{template_name}.json")

@pytest.fixture
def mock_get_file_name(monkeypatch):
    def mock_get_file_name(replay_dir, template_name):
        return os.path.join(replay_dir, f"{template_name}.json")
    monkeypatch.setattr('cookiecutter.replay.get_file_name', mock_get_file_name)

def test_load_with_invalid_template_name_type():
    with pytest.raises(TypeError, match='Template name is required to be of type str'):
        load('/some/dir', 123)

def test_load_with_missing_cookiecutter_key(tmpdir, mock_get_file_name):
    replay_dir = tmpdir.mkdir("replay")
    template_name = "test_template"
    replay_file = replay_dir.join(f"{template_name}.json")
    replay_file.write(json.dumps({"not_cookiecutter": {}}))

    with pytest.raises(ValueError, match='Context is required to contain a cookiecutter key'):
        load(str(replay_dir), template_name)

def test_load_success(tmpdir, mock_get_file_name):
    replay_dir = tmpdir.mkdir("replay")
    template_name = "test_template"
    replay_file = replay_dir.join(f"{template_name}.json")
    expected_context = {"cookiecutter": {"key": "value"}}
    replay_file.write(json.dumps(expected_context))

    context = load(str(replay_dir), template_name)
    assert context == expected_context
