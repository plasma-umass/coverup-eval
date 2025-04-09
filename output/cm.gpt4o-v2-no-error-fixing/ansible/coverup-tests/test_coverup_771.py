# file: lib/ansible/playbook/play_context.py:156-165
# asked: {"lines": [160, 161, 162, 163, 164, 165], "branches": [[161, 0], [161, 162], [162, 161], [162, 163], [164, 161], [164, 165]]}
# gained: {"lines": [160, 161, 162, 163, 164, 165], "branches": [[161, 0], [161, 162], [162, 163], [164, 161], [164, 165]]}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.play_context import PlayContext
from ansible.plugins import get_plugin_class

@pytest.fixture
def mock_plugin():
    plugin = Mock()
    plugin._load_name = 'mock_plugin'
    plugin.get_option = Mock(side_effect=lambda x: f'value_of_{x}')
    return plugin

@pytest.fixture
def play_context():
    return PlayContext()

@patch('ansible.constants.config.get_configuration_definitions')
def test_set_attributes_from_plugin(mock_get_config_defs, play_context, mock_plugin):
    mock_get_config_defs.return_value = {
        'option1': {'name': 'attr1'},
        'option2': {'name': 'attr2'},
        'option3': {'name': None},
        'option4': {'name': 'attr4'}
    }

    play_context.set_attributes_from_plugin(mock_plugin)

    assert getattr(play_context, 'attr1') == 'value_of_attr1'
    assert getattr(play_context, 'attr2') == 'value_of_attr2'
    assert not hasattr(play_context, 'option3')
    assert getattr(play_context, 'attr4') == 'value_of_attr4'
