# file cookiecutter/replay.py:12-16
# lines [12, 14, 15, 16]
# branches []

import os
import pytest
from cookiecutter import replay

@pytest.fixture
def mock_replay_dir(tmp_path):
    return tmp_path

def test_get_file_name_with_json_suffix(mock_replay_dir):
    template_name = "template.json"
    expected_file_path = os.path.join(mock_replay_dir, template_name)
    file_path = replay.get_file_name(mock_replay_dir, template_name)
    assert file_path == expected_file_path

def test_get_file_name_without_json_suffix(mock_replay_dir):
    template_name = "template"
    expected_file_path = os.path.join(mock_replay_dir, template_name + ".json")
    file_path = replay.get_file_name(mock_replay_dir, template_name)
    assert file_path == expected_file_path
