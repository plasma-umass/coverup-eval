# file lib/ansible/playbook/play_context.py:156-165
# lines [160, 161, 162, 163, 164, 165]
# branches ['161->exit', '161->162', '162->161', '162->163', '164->161', '164->165']

import pytest
from ansible.playbook.play_context import PlayContext
from ansible.plugins.loader import connection_loader
from ansible.utils.sentinel import Sentinel
from ansible import constants as C

# Mocking the necessary parts of Ansible to test PlayContext.set_attributes_from_plugin
class MockPlugin:
    _load_name = 'mock_plugin'

    def get_option(self, flag):
        return 'mock_value'

@pytest.fixture
def mock_plugin(mocker):
    plugin = MockPlugin()
    mocker.patch.object(connection_loader, 'get', return_value=plugin)
    return plugin

@pytest.fixture
def mock_config(mocker):
    mocker.patch.object(C.config, 'get_configuration_definitions', return_value={'test_option': {'name': 'test_attribute'}})

def test_set_attributes_from_plugin(mock_plugin, mock_config):
    play_context = PlayContext()
    play_context.set_attributes_from_plugin(mock_plugin)
    assert hasattr(play_context, 'test_attribute')
    assert getattr(play_context, 'test_attribute') == 'mock_value'
