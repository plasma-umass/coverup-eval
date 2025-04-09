# file: lib/ansible/plugins/callback/default.py:380-397
# asked: {"lines": [380, 381, 382, 383, 386, 387, 388, 389, 391, 392, 393, 394, 396, 397], "branches": [[381, 382], [381, 386], [386, 387], [386, 396], [387, 388], [387, 391], [391, 392], [391, 396], [393, 391], [393, 394], [396, 0], [396, 397]]}
# gained: {"lines": [380, 381, 382, 383, 386, 387, 388, 389, 391, 392, 393, 394, 396, 397], "branches": [[381, 382], [381, 386], [386, 387], [386, 396], [387, 388], [387, 391], [391, 392], [391, 396], [393, 391], [393, 394], [396, 0], [396, 397]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C
from ansible import context

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture(autouse=True)
def cliargs_cleanup():
    original_cliargs = context.CLIARGS
    yield
    context.CLIARGS = original_cliargs

def test_v2_playbook_on_start_verbosity_1(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_display.verbosity = 2
    mock_display.banner = MagicMock()
    playbook = MagicMock()
    playbook._file_name = 'test_playbook.yml'

    with patch('os.path.basename', return_value='test_playbook.yml'):
        context.CLIARGS = {'check': False}
        callback_module.v2_playbook_on_start(playbook)

    mock_display.banner.assert_called_once_with("PLAYBOOK: test_playbook.yml")

def test_v2_playbook_on_start_verbosity_3_with_args(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_display.verbosity = 4
    mock_display.display = MagicMock()
    context.CLIARGS = {'args': ['arg1', 'arg2'], 'check': False}

    callback_module.v2_playbook_on_start(MagicMock())

    mock_display.display.assert_any_call('Positional arguments: arg1 arg2', color=C.COLOR_VERBOSE, screen_only=True)

def test_v2_playbook_on_start_verbosity_3_without_args(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_display.verbosity = 4
    mock_display.display = MagicMock()
    context.CLIARGS = {'arg1': 'value1', 'arg2': 'value2', 'check': False}

    callback_module.v2_playbook_on_start(MagicMock())

    mock_display.display.assert_any_call('arg1: value1', color=C.COLOR_VERBOSE, screen_only=True)
    mock_display.display.assert_any_call('arg2: value2', color=C.COLOR_VERBOSE, screen_only=True)

def test_v2_playbook_on_start_check_mode(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_display.verbosity = 1
    mock_display.banner = MagicMock()
    context.CLIARGS = {'check': True}
    callback_module.check_mode_markers = True

    callback_module.v2_playbook_on_start(MagicMock())

    mock_display.banner.assert_called_once_with("DRY RUN")
