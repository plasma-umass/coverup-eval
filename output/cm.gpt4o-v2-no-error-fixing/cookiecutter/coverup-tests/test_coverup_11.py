# file: cookiecutter/replay.py:39-52
# asked: {"lines": [39, 41, 42, 44, 46, 47, 49, 50, 52], "branches": [[41, 42], [41, 44], [49, 50], [49, 52]]}
# gained: {"lines": [39, 41, 42, 44, 46, 47, 49, 50, 52], "branches": [[41, 42], [41, 44], [49, 50], [49, 52]]}

import pytest
import json
import os
from unittest import mock
from cookiecutter.replay import load, get_file_name

def test_load_with_invalid_template_name():
    with pytest.raises(TypeError, match="Template name is required to be of type str"):
        load("some_dir", 123)

def test_load_with_missing_cookiecutter_key(tmpdir):
    replay_dir = tmpdir.mkdir("replay")
    template_name = "template"
    replay_file = replay_dir.join(f"{template_name}.json")
    replay_file.write(json.dumps({"no_cookiecutter": "value"}))

    with pytest.raises(ValueError, match="Context is required to contain a cookiecutter key"):
        load(str(replay_dir), template_name)

def test_load_success(tmpdir):
    replay_dir = tmpdir.mkdir("replay")
    template_name = "template"
    replay_file = replay_dir.join(f"{template_name}.json")
    expected_context = {"cookiecutter": "value"}
    replay_file.write(json.dumps(expected_context))

    context = load(str(replay_dir), template_name)
    assert context == expected_context

def test_load_with_non_json_extension(tmpdir):
    replay_dir = tmpdir.mkdir("replay")
    template_name = "template.txt"
    replay_file = replay_dir.join(f"{template_name}.json")
    expected_context = {"cookiecutter": "value"}
    replay_file.write(json.dumps(expected_context))

    context = load(str(replay_dir), template_name)
    assert context == expected_context
