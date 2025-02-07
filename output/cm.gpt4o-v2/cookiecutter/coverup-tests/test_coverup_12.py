# file: cookiecutter/replay.py:39-52
# asked: {"lines": [39, 41, 42, 44, 46, 47, 49, 50, 52], "branches": [[41, 42], [41, 44], [49, 50], [49, 52]]}
# gained: {"lines": [39, 41, 42, 44, 46, 47, 49, 50, 52], "branches": [[41, 42], [41, 44], [49, 50], [49, 52]]}

import pytest
import json
import os
from unittest import mock

from cookiecutter.replay import load

def test_load_with_invalid_template_name():
    with pytest.raises(TypeError):
        load('some_dir', 123)

def test_load_with_missing_cookiecutter_key(tmp_path):
    replay_dir = tmp_path / "replay"
    replay_dir.mkdir()
    template_name = "template"
    replay_file = replay_dir / "template.json"
    
    with open(replay_file, 'w') as f:
        json.dump({}, f)
    
    with pytest.raises(ValueError):
        load(replay_dir, template_name)

def test_load_success(tmp_path):
    replay_dir = tmp_path / "replay"
    replay_dir.mkdir()
    template_name = "template"
    replay_file = replay_dir / "template.json"
    
    context_data = {"cookiecutter": {"key": "value"}}
    with open(replay_file, 'w') as f:
        json.dump(context_data, f)
    
    context = load(replay_dir, template_name)
    assert context == context_data

def test_load_with_non_json_extension(tmp_path):
    replay_dir = tmp_path / "replay"
    replay_dir.mkdir()
    template_name = "template.txt"
    replay_file = replay_dir / "template.txt.json"
    
    context_data = {"cookiecutter": {"key": "value"}}
    with open(replay_file, 'w') as f:
        json.dump(context_data, f)
    
    context = load(replay_dir, template_name)
    assert context == context_data
