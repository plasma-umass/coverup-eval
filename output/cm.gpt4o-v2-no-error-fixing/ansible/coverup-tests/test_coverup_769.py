# file: lib/ansible/modules/debconf.py:113-126
# asked: {"lines": [113, 114, 115, 117, 118, 120, 122, 123, 124, 126], "branches": [[117, 118], [117, 120], [122, 123], [122, 126]]}
# gained: {"lines": [113, 114, 115, 117, 118, 120, 122, 123, 124, 126], "branches": [[117, 118], [117, 120], [122, 123], [122, 126]]}

import pytest
from unittest.mock import Mock

def test_get_selections_success(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/usr/bin/debconf-show'
    module.run_command.return_value = (0, 'key1: value1\nkey2: value2\n*key3: value3', '')

    from ansible.modules.debconf import get_selections
    result = get_selections(module, 'dummy_pkg')

    assert result == {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }

def test_get_selections_failure(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/usr/bin/debconf-show'
    module.run_command.return_value = (1, '', 'error message')

    module.fail_json = Mock()

    from ansible.modules.debconf import get_selections
    get_selections(module, 'dummy_pkg')

    module.fail_json.assert_called_once_with(msg='error message')
