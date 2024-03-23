# file httpie/plugins/base.py:14-55
# lines [14, 15, 27, 32, 36, 44, 49, 54]
# branches []

import pytest
from httpie.plugins.base import AuthPlugin
from unittest.mock import Mock


class DummyAuthPlugin(AuthPlugin):
    auth_type = 'dummy'


@pytest.fixture
def mock_plugin_manager(mocker):
    plugin_manager = mocker.Mock()
    plugin_manager.get_auth_plugins.return_value = {
        DummyAuthPlugin.auth_type: DummyAuthPlugin()
    }
    return plugin_manager


def test_auth_plugin_attributes(mock_plugin_manager):
    plugin = mock_plugin_manager.get_auth_plugins()[DummyAuthPlugin.auth_type]
    assert plugin.auth_type == 'dummy'
    assert plugin.auth_require is True
    assert plugin.auth_parse is True
    assert plugin.netrc_parse is False
    assert plugin.prompt_password is True
    assert plugin.raw_auth is None
