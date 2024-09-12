# file: cookiecutter/replay.py:12-16
# asked: {"lines": [12, 14, 15, 16], "branches": []}
# gained: {"lines": [12, 14, 15, 16], "branches": []}

import os
import pytest
from cookiecutter.replay import get_file_name

def test_get_file_name_with_json_suffix():
    replay_dir = "/path/to/replay"
    template_name = "template.json"
    expected = os.path.join(replay_dir, template_name)
    assert get_file_name(replay_dir, template_name) == expected

def test_get_file_name_without_json_suffix():
    replay_dir = "/path/to/replay"
    template_name = "template"
    expected = os.path.join(replay_dir, "template.json")
    assert get_file_name(replay_dir, template_name) == expected
