# file lib/ansible/plugins/callback/default.py:64-76
# lines [64, 66, 69, 70, 71, 72, 73, 74, 75, 76]
# branches ['69->exit', '69->70']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.plugins.callback import CallbackBase

# Mocking COMPAT_OPTIONS for the test
COMPAT_OPTIONS = [
    ('option1', 'constant1'),
    ('option2', 'constant2')
]

@pytest.fixture
def mock_display():
    return MagicMock()

@pytest.fixture
def callback_module(mock_display):
    module = CallbackModule()
    module._display = mock_display
    module._load_name = 'test_callback_module'  # Mocking _load_name to avoid AttributeError
    return module

def test_set_options_with_missing_options(callback_module, mocker):
    mocker.patch('ansible.plugins.callback.default.COMPAT_OPTIONS', COMPAT_OPTIONS)
    
    # Mocking get_option to raise AttributeError for the first option and KeyError for the second
    callback_module.get_option = MagicMock(side_effect=[AttributeError, KeyError])
    
    callback_module.set_options()
    
    # Assertions to check if the deprecated message was called twice
    assert callback_module._display.deprecated.call_count == 2
    assert callback_module._display.deprecated.call_args_list[0][0][0] == "'%s' is subclassing DefaultCallback without the corresponding doc_fragment." % callback_module._load_name
    assert callback_module._display.deprecated.call_args_list[1][0][0] == "'%s' is subclassing DefaultCallback without the corresponding doc_fragment." % callback_module._load_name
    
    # Assertions to check if the options were set to the constants
    assert getattr(callback_module, 'option1') == 'constant1'
    assert getattr(callback_module, 'option2') == 'constant2'
