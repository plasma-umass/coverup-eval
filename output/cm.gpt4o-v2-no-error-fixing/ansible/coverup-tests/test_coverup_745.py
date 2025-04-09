# file: lib/ansible/playbook/play_context.py:321-337
# asked: {"lines": [327, 328, 329, 330, 332, 333, 334, 335, 336, 337], "branches": [[327, 0], [327, 328], [329, 330], [329, 332], [333, 327], [333, 334], [334, 333], [334, 335]]}
# gained: {"lines": [327, 328, 329, 330, 332, 333, 334, 335], "branches": [[327, 0], [327, 328], [329, 330], [329, 332], [333, 327], [333, 334], [334, 335]]}

import pytest
from ansible.playbook.play_context import PlayContext
from unittest.mock import MagicMock

@pytest.fixture
def play_context():
    return PlayContext()

def test_update_vars(play_context, monkeypatch):
    # Mock the MAGIC_VARIABLE_MAPPING to ensure coverage
    mock_magic_var_mapping = {
        'attr1': ['var1', 'var2'],
        'attr2': ['var3'],
        'become_attr': ['var4']
    }
    monkeypatch.setattr('ansible.constants.MAGIC_VARIABLE_MAPPING', mock_magic_var_mapping)

    # Set attributes on the play_context
    setattr(play_context, 'attr1', 'value1')
    setattr(play_context, 'attr2', 'value2')
    setattr(play_context, 'become_attr', 'value3')

    variables = {}

    play_context.update_vars(variables)

    # Assertions to verify the correct variables are set
    assert variables['var1'] == 'value1'
    assert variables['var2'] == 'value1'
    assert variables['var3'] == 'value2'
    assert 'var4' not in variables  # 'become' in prop should skip this

    # Clean up
    delattr(play_context, 'attr1')
    delattr(play_context, 'attr2')
    delattr(play_context, 'become_attr')
