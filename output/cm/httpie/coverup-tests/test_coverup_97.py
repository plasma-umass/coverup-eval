# file httpie/plugins/base.py:56-67
# lines [67]
# branches []

import pytest
from httpie.plugins.base import AuthPlugin

@pytest.fixture
def auth_plugin():
    return AuthPlugin()

def test_get_auth_executes_missing_line(auth_plugin):
    with pytest.raises(NotImplementedError):
        auth_plugin.get_auth()
