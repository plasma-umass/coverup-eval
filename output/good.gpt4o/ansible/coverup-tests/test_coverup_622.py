# file lib/ansible/plugins/callback/default.py:45-55
# lines [45, 47, 52, 53, 54]
# branches []

import pytest
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_callback_module_attributes(callback_module):
    assert callback_module.CALLBACK_VERSION == 2.0
    assert callback_module.CALLBACK_TYPE == 'stdout'
    assert callback_module.CALLBACK_NAME == 'default'
