# file: lib/ansible/playbook/play.py:315-320
# asked: {"lines": [316, 317, 318, 319, 320], "branches": [[316, 317], [316, 318], [318, 319], [318, 320]]}
# gained: {"lines": [316, 317, 318, 319, 320], "branches": [[316, 317], [316, 318], [318, 319], [318, 320]]}

import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    return Play()

def test_get_vars_files_none(play_instance):
    play_instance.vars_files = None
    assert play_instance.get_vars_files() == []

def test_get_vars_files_not_list(play_instance):
    play_instance.vars_files = "not_a_list"
    assert play_instance.get_vars_files() == ["not_a_list"]

def test_get_vars_files_list(play_instance):
    play_instance.vars_files = ["file1", "file2"]
    assert play_instance.get_vars_files() == ["file1", "file2"]
