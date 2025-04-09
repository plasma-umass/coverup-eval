# file httpie/plugins/base.py:14-55
# lines [14, 15, 27, 32, 36, 44, 49, 54]
# branches []

import pytest
from httpie.plugins.base import AuthPlugin

def test_auth_plugin_attributes():
    class MyAuthPlugin(AuthPlugin):
        auth_type = "my-auth"
        auth_require = False
        auth_parse = False
        netrc_parse = True
        prompt_password = False

    plugin = MyAuthPlugin()

    assert plugin.auth_type == "my-auth"
    assert plugin.auth_require is False
    assert plugin.auth_parse is False
    assert plugin.netrc_parse is True
    assert plugin.prompt_password is False
    assert plugin.raw_auth is None

@pytest.fixture
def mock_auth_plugin(mocker):
    class MockAuthPlugin(AuthPlugin):
        auth_type = "mock-auth"
        auth_require = True
        auth_parse = True
        netrc_parse = False
        prompt_password = True

    return MockAuthPlugin()

def test_auth_plugin_with_mock(mock_auth_plugin):
    assert mock_auth_plugin.auth_type == "mock-auth"
    assert mock_auth_plugin.auth_require is True
    assert mock_auth_plugin.auth_parse is True
    assert mock_auth_plugin.netrc_parse is False
    assert mock_auth_plugin.prompt_password is True
    assert mock_auth_plugin.raw_auth is None
