# file: lib/ansible/plugins/callback/default.py:64-76
# asked: {"lines": [66, 69, 70, 71, 72, 73, 74, 75, 76], "branches": [[69, 0], [69, 70]]}
# gained: {"lines": [66, 69, 70, 71, 72, 73, 74, 75, 76], "branches": [[69, 0], [69, 70]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._display = MagicMock()
    module._load_name = 'default'
    return module

def test_set_options_executes_all_lines(callback_module, monkeypatch):
    # Mocking the necessary parts
    mock_get_plugin_options = MagicMock(return_value={'display_skipped_hosts': True})
    monkeypatch.setattr(C.config, 'get_plugin_options', mock_get_plugin_options)
    
    mock_get_option = MagicMock(side_effect=lambda k: {'display_skipped_hosts': True}[k])
    monkeypatch.setattr(callback_module, 'get_option', mock_get_option)
    
    # Mocking COMPAT_OPTIONS
    compat_options = [
        ('display_skipped_hosts', C.DISPLAY_SKIPPED_HOSTS),
        ('display_ok_hosts', True),
        ('show_custom_stats', C.SHOW_CUSTOM_STATS),
        ('display_failed_stderr', False),
        ('check_mode_markers', False),
        ('show_per_host_start', False)
    ]
    monkeypatch.setattr('ansible.plugins.callback.default.COMPAT_OPTIONS', compat_options)
    
    # Execute the method
    callback_module.set_options()
    
    # Assertions to ensure all lines are executed
    mock_get_plugin_options.assert_called_once()
    assert callback_module.display_skipped_hosts is True
    assert callback_module.display_ok_hosts is True
    assert callback_module.show_custom_stats == C.SHOW_CUSTOM_STATS
    assert callback_module.display_failed_stderr is False
    assert callback_module.check_mode_markers is False
    assert callback_module.show_per_host_start is False

    # Ensure deprecated warning is called
    callback_module._display.deprecated.assert_called_with(
        "'default' is subclassing DefaultCallback without the corresponding doc_fragment.",
        version='2.14', collection_name='ansible.builtin'
    )
