# file lib/ansible/playbook/play_context.py:156-165
# lines [156, 160, 161, 162, 163, 164, 165]
# branches ['161->exit', '161->162', '162->161', '162->163', '164->161', '164->165']

import pytest
from ansible.playbook.play_context import PlayContext
from ansible.plugins.loader import connection_loader
from ansible.utils.sentinel import Sentinel
from ansible import constants as C

# Mocking the necessary parts of the plugin
class MockPlugin:
    def __init__(self, options):
        self._load_name = 'mock_plugin'
        self.options = options

    def get_option(self, flag):
        return self.options.get(flag, Sentinel)

@pytest.fixture
def mock_plugin(mocker):
    options = {'test_option': 'test_value'}
    plugin = MockPlugin(options)
    mocker.patch.object(connection_loader, 'get', return_value=plugin)
    mocker.patch.object(C.config, 'get_configuration_definitions', return_value={'test_option': {'name': 'test_option'}})
    return plugin

def test_set_attributes_from_plugin(mock_plugin):
    play_context = PlayContext()

    # Before setting attributes from plugin
    assert not hasattr(play_context, 'test_option')

    # Set attributes from plugin
    play_context.set_attributes_from_plugin(mock_plugin)

    # After setting attributes from plugin
    assert hasattr(play_context, 'test_option')
    assert play_context.test_option == 'test_value'
