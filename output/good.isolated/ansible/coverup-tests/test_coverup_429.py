# file lib/ansible/playbook/play.py:315-320
# lines [315, 316, 317, 318, 319, 320]
# branches ['316->317', '316->318', '318->319', '318->320']

import pytest
from ansible.playbook.play import Play

# Assuming the Play class is part of a larger module and has dependencies,
# we will mock out any necessary parts to isolate the test.

@pytest.fixture
def mock_play(mocker):
    # Mocking the Base and CollectionSearch parts of the Play class
    mocker.patch('ansible.playbook.play.Base')
    mocker.patch('ansible.playbook.play.CollectionSearch')
    mocker.patch('ansible.playbook.play.Taggable')
    return Play()

def test_get_vars_files_with_none(mock_play):
    mock_play.vars_files = None
    assert mock_play.get_vars_files() == []

def test_get_vars_files_with_non_list(mock_play):
    mock_play.vars_files = "vars_file.yml"
    assert mock_play.get_vars_files() == ["vars_file.yml"]

def test_get_vars_files_with_list(mock_play):
    mock_play.vars_files = ["vars_file1.yml", "vars_file2.yml"]
    assert mock_play.get_vars_files() == ["vars_file1.yml", "vars_file2.yml"]
