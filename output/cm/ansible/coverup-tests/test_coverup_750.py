# file lib/ansible/plugins/callback/junit.py:276-278
# lines [276, 277, 278]
# branches []

import os
import pytest
from ansible.plugins.callback import junit
from ansible.playbook.play import Play

# Assuming the CallbackModule is in a file named junit.py under ansible/plugins/callback/
# and the class is named CallbackModule as shown in the provided code snippet.

@pytest.fixture
def playbook(tmp_path):
    # Create a temporary playbook file to simulate playbook._file_name
    p = tmp_path / "test_playbook.yml"
    p.write_text("---\n- hosts: all\n  tasks:\n    - debug:\n        msg: 'Test playbook'")
    return p

@pytest.fixture
def callback_module():
    return junit.CallbackModule()

def test_v2_playbook_on_start(playbook, callback_module, mocker):
    # Mock the Playbook object to have a _file_name attribute
    mock_playbook = mocker.Mock()
    mock_playbook._file_name = str(playbook)

    # Call the method we want to test
    callback_module.v2_playbook_on_start(mock_playbook)

    # Assert that the playbook name and path are set correctly
    assert callback_module._playbook_path == str(playbook)
    assert callback_module._playbook_name == os.path.splitext(os.path.basename(str(playbook)))[0]

    # Clean up the temporary playbook file
    playbook.unlink()
