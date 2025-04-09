# file: lib/ansible/plugins/callback/default.py:324-378
# asked: {"lines": [324, 325, 327, 328, 329, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 342, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 356, 359, 362, 363, 366, 367, 368, 369, 372, 373, 374, 375, 377, 378], "branches": [[328, 329], [328, 359], [362, 363], [362, 377], [366, 367], [366, 372], [367, 368], [367, 369], [372, 373], [372, 375], [377, 0], [377, 378]]}
# gained: {"lines": [324, 325, 327, 328, 329, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 342, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 356, 359, 362, 363, 366, 367, 368, 369, 372, 373, 374, 375, 377, 378], "branches": [[328, 329], [328, 359], [362, 363], [366, 367], [366, 372], [367, 368], [367, 369], [372, 373], [377, 378]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.display import Display

@pytest.fixture
def callback_module():
    cb = CallbackModule()
    cb._display = Display()
    cb.show_custom_stats = True
    return cb

def test_v2_playbook_on_stats(callback_module, monkeypatch):
    stats = MagicMock()
    stats.processed = {
        'host1': {},
        'host2': {}
    }
    stats.summarize = MagicMock(side_effect=[
        {'ok': 1, 'changed': 2, 'unreachable': 0, 'failures': 1, 'skipped': 1, 'rescued': 0, 'ignored': 0},
        {'ok': 2, 'changed': 1, 'unreachable': 0, 'failures': 0, 'skipped': 0, 'rescued': 1, 'ignored': 1}
    ])
    stats.custom = {
        'custom_stat1': 'value1',
        '_run': 'run_value'
    }

    monkeypatch.setattr('ansible.context.CLIARGS', {'check': True})
    callback_module.check_mode_markers = True

    with patch.object(callback_module._display, 'banner') as mock_banner, \
         patch.object(callback_module._display, 'display') as mock_display, \
         patch.object(callback_module, '_dump_results', return_value='dumped_result'):
        
        callback_module.v2_playbook_on_stats(stats)

        # Assertions for banner calls
        mock_banner.assert_any_call("PLAY RECAP")
        mock_banner.assert_any_call("CUSTOM STATS: ")
        mock_banner.assert_any_call("DRY RUN")

        # Assertions for display calls
        assert mock_display.call_count == 9
        mock_display.assert_any_call("host1                      : ok=1    changed=2    unreachable=0    failed=1    skipped=1    rescued=0    ignored=0   ", screen_only=True)
        mock_display.assert_any_call("host2                      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=1    ignored=1   ", screen_only=True)
        mock_display.assert_any_call("host1                      : ok=1    changed=2    unreachable=0    failed=1    skipped=1    rescued=0    ignored=0   ", log_only=True)
        mock_display.assert_any_call("host2                      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=1    ignored=1   ", log_only=True)
        mock_display.assert_any_call("", screen_only=True)
        mock_display.assert_any_call("\tcustom_stat1: dumped_result")
        mock_display.assert_any_call("", screen_only=True)
        mock_display.assert_any_call("\tRUN: dumped_result")
        mock_display.assert_any_call("", screen_only=True)
