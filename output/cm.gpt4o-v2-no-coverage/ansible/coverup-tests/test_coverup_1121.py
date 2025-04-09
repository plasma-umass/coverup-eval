# file: lib/ansible/modules/debconf.py:129-142
# asked: {"lines": [129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 142], "branches": [[132, 133], [132, 135], [135, 136], [135, 140], [136, 137], [136, 138], [138, 139], [138, 140]]}
# gained: {"lines": [129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 142], "branches": [[132, 133], [132, 135], [135, 136], [135, 140], [136, 137], [136, 138], [138, 139]]}

import pytest
from unittest.mock import Mock

def test_set_selection_boolean_true(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/usr/bin/debconf-set-selections'
    module.run_command.return_value = (0, '', '')

    from ansible.modules.debconf import set_selection

    result = set_selection(module, 'pkg', 'question', 'boolean', 'True', False)
    assert result == (0, '', '')
    module.get_bin_path.assert_called_once_with('debconf-set-selections', True)
    module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections'], data='pkg question boolean true')

def test_set_selection_boolean_false(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/usr/bin/debconf-set-selections'
    module.run_command.return_value = (0, '', '')

    from ansible.modules.debconf import set_selection

    result = set_selection(module, 'pkg', 'question', 'boolean', 'False', False)
    assert result == (0, '', '')
    module.get_bin_path.assert_called_once_with('debconf-set-selections', True)
    module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections'], data='pkg question boolean false')

def test_set_selection_unseen(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/usr/bin/debconf-set-selections'
    module.run_command.return_value = (0, '', '')

    from ansible.modules.debconf import set_selection

    result = set_selection(module, 'pkg', 'question', 'string', 'value', True)
    assert result == (0, '', '')
    module.get_bin_path.assert_called_once_with('debconf-set-selections', True)
    module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections', '-u'], data='pkg question string value')

def test_set_selection_default(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/usr/bin/debconf-set-selections'
    module.run_command.return_value = (0, '', '')

    from ansible.modules.debconf import set_selection

    result = set_selection(module, 'pkg', 'question', 'string', 'value', False)
    assert result == (0, '', '')
    module.get_bin_path.assert_called_once_with('debconf-set-selections', True)
    module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections'], data='pkg question string value')
