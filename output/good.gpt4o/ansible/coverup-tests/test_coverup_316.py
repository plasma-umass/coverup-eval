# file lib/ansible/playbook/play_context.py:156-165
# lines [156, 160, 161, 162, 163, 164, 165]
# branches ['161->exit', '161->162', '162->161', '162->163', '164->161', '164->165']

import pytest
from unittest.mock import Mock, patch

# Assuming the necessary imports and setup for PlayContext and other dependencies
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def mock_plugin():
    plugin = Mock()
    plugin._load_name = 'mock_plugin'
    plugin.get_option = Mock(side_effect=lambda x: f'value_of_{x}')
    return plugin

@pytest.fixture
def play_context():
    return PlayContext()

def test_set_attributes_from_plugin(play_context, mock_plugin):
    with patch('ansible.playbook.play_context.C.config.get_configuration_definitions') as mock_get_config_defs:
        mock_get_config_defs.return_value = {
            'option1': {'name': 'attr1'},
            'option2': {'name': 'attr2'},
            'option3': {'name': None},  # This should be skipped
        }

        play_context.set_attributes_from_plugin(mock_plugin)

        assert getattr(play_context, 'attr1') == 'value_of_attr1'
        assert getattr(play_context, 'attr2') == 'value_of_attr2'
        assert not hasattr(play_context, 'option3')  # Ensure 'option3' is not set

        # Clean up
        delattr(play_context, 'attr1')
        delattr(play_context, 'attr2')
