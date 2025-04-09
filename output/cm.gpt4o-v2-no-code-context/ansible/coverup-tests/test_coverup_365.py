# file: lib/ansible/playbook/play.py:315-320
# asked: {"lines": [315, 316, 317, 318, 319, 320], "branches": [[316, 317], [316, 318], [318, 319], [318, 320]]}
# gained: {"lines": [315, 316, 317, 318, 319, 320], "branches": [[316, 317], [316, 318], [318, 319], [318, 320]]}

import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    class MockPlay(Play):
        def __init__(self, vars_files):
            self.vars_files = vars_files

    return MockPlay

def test_get_vars_files_none(play_instance):
    play = play_instance(None)
    assert play.get_vars_files() == []

def test_get_vars_files_not_list(play_instance):
    play = play_instance('vars_file.yml')
    assert play.get_vars_files() == ['vars_file.yml']

def test_get_vars_files_list(play_instance):
    play = play_instance(['vars_file1.yml', 'vars_file2.yml'])
    assert play.get_vars_files() == ['vars_file1.yml', 'vars_file2.yml']
