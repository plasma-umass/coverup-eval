# file lib/ansible/plugins/callback/default.py:64-76
# lines [64, 66, 69, 70, 71, 72, 73, 74, 75, 76]
# branches ['69->exit', '69->70']

import pytest
from ansible.plugins.callback import default
from ansible.utils.display import Display

# Mocking the COMPAT_OPTIONS to test the fallback mechanism
default.COMPAT_OPTIONS = [('test_option', 'default_value')]

class TestCallbackModule(default.CallbackModule):
    def __init__(self):
        display = Display()
        super(TestCallbackModule, self).__init__()

def test_set_options_with_missing_option(mocker):
    mocker.patch('ansible.plugins.callback.default.CallbackBase.set_options')
    mocker.patch.object(Display, 'deprecated')

    callback = TestCallbackModule()
    callback._load_name = 'test_callback'  # Set a dummy _load_name for the deprecation message
    callback.set_options()

    # Check that the fallback value is set correctly
    assert callback.test_option == 'default_value'
    # Check that the deprecation warning was called
    Display.deprecated.assert_called_once()
