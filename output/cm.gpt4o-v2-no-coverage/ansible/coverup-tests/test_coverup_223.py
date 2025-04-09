# file: lib/ansible/playbook/play_context.py:321-337
# asked: {"lines": [321, 327, 328, 329, 330, 332, 333, 334, 335, 336, 337], "branches": [[327, 0], [327, 328], [329, 330], [329, 332], [333, 327], [333, 334], [334, 333], [334, 335]]}
# gained: {"lines": [321, 327, 328, 329, 330, 332, 333, 334, 335, 336, 337], "branches": [[327, 0], [327, 328], [329, 330], [329, 332], [333, 327], [333, 334], [334, 335]]}

import pytest
from ansible.playbook.play_context import PlayContext
from unittest.mock import MagicMock

@pytest.fixture
def play_context():
    return PlayContext()

def test_update_vars(play_context, monkeypatch):
    # Mock the MAGIC_VARIABLE_MAPPING
    magic_var_mapping = {
        'connection': ['ansible_connection', 'ansible_host'],
        'remote_user': ['ansible_user'],
        'become': ['ansible_become'],
    }
    monkeypatch.setattr('ansible.constants.MAGIC_VARIABLE_MAPPING', magic_var_mapping)

    # Set attributes on the play_context
    play_context.connection = 'ssh'
    play_context.remote_user = 'root'
    play_context.become = True

    variables = {}
    play_context.update_vars(variables)

    # Assertions to verify the correct variables are set
    assert variables['ansible_connection'] == 'ssh'
    assert variables['ansible_user'] == 'root'
    assert 'ansible_become' not in variables  # 'become' should be skipped

def test_update_vars_with_missing_attribute(play_context, monkeypatch):
    # Mock the MAGIC_VARIABLE_MAPPING
    magic_var_mapping = {
        'missing_attr': ['ansible_missing_attr'],
    }
    monkeypatch.setattr('ansible.constants.MAGIC_VARIABLE_MAPPING', magic_var_mapping)

    variables = {}
    play_context.update_vars(variables)

    # Assertions to verify that missing attributes are handled gracefully
    assert 'ansible_missing_attr' not in variables
