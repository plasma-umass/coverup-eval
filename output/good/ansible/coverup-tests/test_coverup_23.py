# file lib/ansible/plugins/callback/default.py:324-378
# lines [324, 325, 327, 328, 329, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 342, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 356, 359, 362, 363, 366, 367, 368, 369, 372, 373, 374, 375, 377, 378]
# branches ['328->329', '328->359', '362->363', '362->377', '366->367', '366->372', '367->368', '367->369', '372->373', '372->375', '377->exit', '377->378']

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.executor.stats import AggregateStats
from ansible.utils.display import Display
from ansible import context
from unittest.mock import MagicMock

# Mock the constants used in the module
class C:
    COLOR_OK = 'green'
    COLOR_CHANGED = 'yellow'
    COLOR_UNREACHABLE = 'red'
    COLOR_ERROR = 'bright red'
    COLOR_SKIP = 'cyan'
    COLOR_WARN = 'bright purple'

# Mock the colorize function
def colorize(color_key, msg, color):
    return f"{color_key.upper()}({msg})"

# Mock the hostcolor function
def hostcolor(host, stats, colored=True):
    return f"COLOR({host})" if colored else host

# Inject the mocks into the module
@pytest.fixture(autouse=True)
def mock_dependencies(mocker):
    mocker.patch('ansible.plugins.callback.default.C', new=C)
    mocker.patch('ansible.plugins.callback.default.colorize', side_effect=colorize)
    mocker.patch('ansible.plugins.callback.default.hostcolor', side_effect=hostcolor)

@pytest.fixture
def callback_module():
    display = Display()
    display.banner = MagicMock()
    display.display = MagicMock()
    module = CallbackModule()
    module._display = display
    module.show_custom_stats = True
    module.check_mode_markers = True
    return module

def test_v2_playbook_on_stats(callback_module):
    stats = AggregateStats()
    stats.summarize = MagicMock(return_value={
        'ok': 1, 'changed': 2, 'unreachable': 0, 'failures': 1,
        'skipped': 0, 'rescued': 0, 'ignored': 0
    })
    stats.processed = {'host1': True, 'host2': True}
    stats.custom = {'_run': {'some': 'data'}, 'host_specific': {'info': 'details'}}

    # Mock CLIARGS
    context.CLIARGS = {'check': True}

    callback_module.v2_playbook_on_stats(stats)

    # Assertions to check if the display function was called with the expected values
    callback_module._display.banner.assert_any_call("PLAY RECAP")
    callback_module._display.banner.assert_any_call("DRY RUN")

    # Clean up the context
    del context.CLIARGS
