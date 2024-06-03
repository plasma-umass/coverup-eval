# file lib/ansible/plugins/action/reboot.py:26-75
# lines [26, 27, 28, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 56, 57, 58, 59, 60, 63, 64, 65, 68, 69, 70, 71, 72, 73, 74, 75]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module():
    return ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=MagicMock())

def test_default_values(action_module):
    assert action_module.DEFAULT_REBOOT_TIMEOUT == 600
    assert action_module.DEFAULT_CONNECT_TIMEOUT is None
    assert action_module.DEFAULT_PRE_REBOOT_DELAY == 0
    assert action_module.DEFAULT_POST_REBOOT_DELAY == 0
    assert action_module.DEFAULT_TEST_COMMAND == 'whoami'
    assert action_module.DEFAULT_BOOT_TIME_COMMAND == 'cat /proc/sys/kernel/random/boot_id'
    assert action_module.DEFAULT_REBOOT_MESSAGE == 'Reboot initiated by Ansible'
    assert action_module.DEFAULT_SHUTDOWN_COMMAND == 'shutdown'
    assert action_module.DEFAULT_SHUTDOWN_COMMAND_ARGS == '-r {delay_min} "{message}"'
    assert action_module.DEFAULT_SUDOABLE is True

def test_valid_args(action_module):
    expected_args = frozenset((
        'boot_time_command',
        'connect_timeout',
        'msg',
        'post_reboot_delay',
        'pre_reboot_delay',
        'reboot_command',
        'reboot_timeout',
        'search_paths',
        'test_command',
    ))
    assert action_module._VALID_ARGS == expected_args

def test_boot_time_commands(action_module):
    expected_boot_time_commands = {
        'freebsd': '/sbin/sysctl kern.boottime',
        'openbsd': '/sbin/sysctl kern.boottime',
        'macosx': 'who -b',
        'solaris': 'who -b',
        'sunos': 'who -b',
        'vmkernel': 'grep booted /var/log/vmksummary.log | tail -n 1',
        'aix': 'who -b',
    }
    assert action_module.BOOT_TIME_COMMANDS == expected_boot_time_commands

def test_shutdown_commands(action_module):
    expected_shutdown_commands = {
        'alpine': 'reboot',
        'vmkernel': 'reboot',
    }
    assert action_module.SHUTDOWN_COMMANDS == expected_shutdown_commands

def test_shutdown_command_args(action_module):
    expected_shutdown_command_args = {
        'alpine': '',
        'void': '-r +{delay_min} "{message}"',
        'freebsd': '-r +{delay_sec}s "{message}"',
        'linux': action_module.DEFAULT_SHUTDOWN_COMMAND_ARGS,
        'macosx': '-r +{delay_min} "{message}"',
        'openbsd': '-r +{delay_min} "{message}"',
        'solaris': '-y -g {delay_sec} -i 6 "{message}"',
        'aix': '-Fr',
        'sunos': '-y -g {delay_sec} -i 6 "{message}"',
        'vmkernel': '-d {delay_sec}',
    }
    assert action_module.SHUTDOWN_COMMAND_ARGS == expected_shutdown_command_args

def test_deprecated_args(action_module):
    assert action_module.DEPRECATED_ARGS == {}
