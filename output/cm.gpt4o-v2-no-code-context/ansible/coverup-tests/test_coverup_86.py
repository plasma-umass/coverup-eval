# file: lib/ansible/plugins/callback/default.py:380-397
# asked: {"lines": [380, 381, 382, 383, 386, 387, 388, 389, 391, 392, 393, 394, 396, 397], "branches": [[381, 382], [381, 386], [386, 387], [386, 396], [387, 388], [387, 391], [391, 392], [391, 396], [393, 391], [393, 394], [396, 0], [396, 397]]}
# gained: {"lines": [380, 381, 382, 383, 386, 387, 388, 389, 391, 392, 393, 394, 396, 397], "branches": [[381, 382], [386, 387], [387, 388], [391, 392], [391, 396], [393, 394], [396, 397]]}

import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def callback_module():
    from ansible.plugins.callback.default import CallbackModule
    return CallbackModule()

@pytest.fixture
def mock_display():
    mock_display = MagicMock()
    mock_display.verbosity = 4
    mock_display.COLOR_VERBOSE = 'blue'
    return mock_display

@pytest.fixture
def mock_context():
    with patch('ansible.plugins.callback.default.context', autospec=True) as mock_context:
        mock_context.CLIARGS = {
            'args': ['arg1', 'arg2'],
            'check': True,
            'some_other_arg': 'value'
        }
        yield mock_context

@pytest.fixture
def mock_playbook():
    mock_playbook = MagicMock()
    mock_playbook._file_name = '/path/to/playbook.yml'
    return mock_playbook

def test_v2_playbook_on_start(callback_module, mock_display, mock_context, mock_playbook):
    callback_module._display = mock_display
    callback_module.check_mode_markers = True

    with patch('os.path.basename', return_value='playbook.yml'):
        callback_module.v2_playbook_on_start(mock_playbook)

    mock_display.banner.assert_any_call("PLAYBOOK: playbook.yml")
    mock_display.display.assert_any_call('Positional arguments: arg1 arg2', color='blue', screen_only=True)
    mock_display.display.assert_any_call('some_other_arg: value', color='blue', screen_only=True)
    mock_display.banner.assert_any_call("DRY RUN")
