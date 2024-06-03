# file lib/ansible/plugins/callback/default.py:380-397
# lines [380, 381, 382, 383, 386, 387, 388, 389, 391, 392, 393, 394, 396, 397]
# branches ['381->382', '381->386', '386->387', '386->396', '387->388', '387->391', '391->392', '391->396', '393->391', '393->394', '396->exit', '396->397']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import context
from ansible.utils.display import Display

@pytest.fixture
def mock_display():
    display = MagicMock(spec=Display)
    display.verbosity = 4
    display.COLOR_VERBOSE = 'blue'
    return display

@pytest.fixture
def mock_context():
    original_cliargs = context.CLIARGS
    context.CLIARGS = {
        'args': ['arg1', 'arg2'],
        'check': True,
        'some_other_arg': 'value'
    }
    yield
    context.CLIARGS = original_cliargs

@pytest.fixture
def mock_playbook():
    playbook = MagicMock()
    playbook._file_name = '/path/to/playbook.yml'
    return playbook

def test_v2_playbook_on_start(mock_display, mock_context, mock_playbook):
    callback = CallbackModule()
    callback._display = mock_display
    callback.check_mode_markers = True

    with patch('os.path.basename', return_value='playbook.yml'):
        callback.v2_playbook_on_start(mock_playbook)

    mock_display.banner.assert_any_call("PLAYBOOK: playbook.yml")
    mock_display.display.assert_any_call('Positional arguments: arg1 arg2', color='blue', screen_only=True)
    mock_display.display.assert_any_call('some_other_arg: value', color='blue', screen_only=True)
    mock_display.banner.assert_any_call("DRY RUN")
