# file: cookiecutter/replay.py:12-16
# asked: {"lines": [12, 14, 15, 16], "branches": []}
# gained: {"lines": [12, 14, 15, 16], "branches": []}

import os
import pytest

from cookiecutter.replay import get_file_name

def test_get_file_name_with_json_suffix(monkeypatch):
    replay_dir = '/fake/dir'
    template_name = 'template'
    
    expected_path = os.path.join(replay_dir, 'template.json')
    
    result = get_file_name(replay_dir, template_name)
    
    assert result == expected_path

def test_get_file_name_without_json_suffix(monkeypatch):
    replay_dir = '/fake/dir'
    template_name = 'template.json'
    
    expected_path = os.path.join(replay_dir, 'template.json')
    
    result = get_file_name(replay_dir, template_name)
    
    assert result == expected_path
