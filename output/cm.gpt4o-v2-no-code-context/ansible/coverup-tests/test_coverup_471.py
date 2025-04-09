# file: lib/ansible/playbook/play_context.py:170-185
# asked: {"lines": [170, 176, 177, 181, 182, 185], "branches": [[176, 177], [176, 181]]}
# gained: {"lines": [170, 176, 177, 181, 182, 185], "branches": [[176, 177], [176, 181]]}

import pytest
from unittest.mock import patch

# Assuming the PlayContext class is imported from ansible.playbook.play_context
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def play_context():
    return PlayContext()

def test_set_attributes_from_cli_timeout(play_context, monkeypatch):
    monkeypatch.setattr('ansible.playbook.play_context.context.CLIARGS', {'timeout': '30'})
    play_context.set_attributes_from_cli()
    assert play_context.timeout == 30

def test_set_attributes_from_cli_private_key_file(play_context, monkeypatch):
    monkeypatch.setattr('ansible.playbook.play_context.context.CLIARGS', {'private_key_file': '/path/to/key'})
    play_context.set_attributes_from_cli()
    assert play_context.private_key_file == '/path/to/key'

def test_set_attributes_from_cli_verbosity(play_context, monkeypatch):
    monkeypatch.setattr('ansible.playbook.play_context.context.CLIARGS', {'verbosity': 2})
    play_context.set_attributes_from_cli()
    assert play_context.verbosity == 2

def test_set_attributes_from_cli_start_at_task(play_context, monkeypatch):
    monkeypatch.setattr('ansible.playbook.play_context.context.CLIARGS', {'start_at_task': 'my_task'})
    play_context.set_attributes_from_cli()
    assert play_context.start_at_task == 'my_task'

def test_set_attributes_from_cli_defaults(play_context, monkeypatch):
    monkeypatch.setattr('ansible.playbook.play_context.context.CLIARGS', {})
    play_context.set_attributes_from_cli()
    assert play_context.timeout == 0
    assert play_context.private_key_file is None
    assert play_context.verbosity is None
    assert play_context.start_at_task is None
