# file: lib/ansible/plugins/callback/default.py:306-315
# asked: {"lines": [307, 308, 309, 311, 312, 313, 314, 315], "branches": [[307, 0], [307, 308], [308, 309], [308, 311], [313, 314], [313, 315]]}
# gained: {"lines": [307, 308, 309, 311, 312, 313, 314, 315], "branches": [[307, 0], [307, 308], [308, 309], [308, 311], [313, 314], [313, 315]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule, C

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def result():
    result = MagicMock()
    result._task._uuid = "task-uuid"
    result._task.action = "action"
    result._host.get_name.return_value = "host-name"
    result._result = {"item": "item-value"}
    return result

def test_v2_runner_item_on_skipped_display_skipped_hosts(callback_module, result, monkeypatch):
    callback_module.display_skipped_hosts = True
    callback_module._last_task_banner = "different-uuid"
    
    monkeypatch.setattr(callback_module, '_print_task_banner', MagicMock())
    monkeypatch.setattr(callback_module, '_clean_results', MagicMock())
    monkeypatch.setattr(callback_module, '_get_item_label', lambda x: "item-label")
    monkeypatch.setattr(callback_module, '_run_is_verbose', lambda x: False)
    monkeypatch.setattr(callback_module._display, 'display', MagicMock())
    
    callback_module.v2_runner_item_on_skipped(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._display.display.assert_called_once_with("skipping: [host-name] => (item=item-label) ", color=C.COLOR_SKIP)

def test_v2_runner_item_on_skipped_verbose(callback_module, result, monkeypatch):
    callback_module.display_skipped_hosts = True
    callback_module._last_task_banner = result._task._uuid
    
    monkeypatch.setattr(callback_module, '_print_task_banner', MagicMock())
    monkeypatch.setattr(callback_module, '_clean_results', MagicMock())
    monkeypatch.setattr(callback_module, '_get_item_label', lambda x: "item-label")
    monkeypatch.setattr(callback_module, '_run_is_verbose', lambda x: True)
    monkeypatch.setattr(callback_module, '_dump_results', lambda x: "dumped-results")
    monkeypatch.setattr(callback_module._display, 'display', MagicMock())
    
    callback_module.v2_runner_item_on_skipped(result)
    
    callback_module._print_task_banner.assert_not_called()
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._display.display.assert_called_once_with("skipping: [host-name] => (item=item-label)  => dumped-results", color=C.COLOR_SKIP)

def test_v2_runner_item_on_skipped_no_display_skipped_hosts(callback_module, result, monkeypatch):
    callback_module.display_skipped_hosts = False
    
    monkeypatch.setattr(callback_module, '_print_task_banner', MagicMock())
    monkeypatch.setattr(callback_module, '_clean_results', MagicMock())
    monkeypatch.setattr(callback_module, '_get_item_label', lambda x: "item-label")
    monkeypatch.setattr(callback_module, '_run_is_verbose', lambda x: True)
    monkeypatch.setattr(callback_module, '_dump_results', lambda x: "dumped-results")
    monkeypatch.setattr(callback_module._display, 'display', MagicMock())
    
    callback_module.v2_runner_item_on_skipped(result)
    
    callback_module._print_task_banner.assert_not_called()
    callback_module._clean_results.assert_not_called()
    callback_module._display.display.assert_not_called()
