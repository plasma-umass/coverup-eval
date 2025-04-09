# file: lib/ansible/modules/debconf.py:113-126
# asked: {"lines": [113, 114, 115, 117, 118, 120, 122, 123, 124, 126], "branches": [[117, 118], [117, 120], [122, 123], [122, 126]]}
# gained: {"lines": [113, 114, 115, 117, 118, 120, 122, 123, 124, 126], "branches": [[117, 118], [117, 120], [122, 123], [122, 126]]}

import pytest
from unittest.mock import Mock

# Assuming the function get_selections is imported from the module
# from ansible.modules.debconf import get_selections

def test_get_selections_success(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/usr/bin/debconf-show'
    module.run_command.return_value = (0, 'key1: value1\nkey2: value2\n*key3: value3', '')

    pkg = 'some-package'
    expected_selections = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }

    from ansible.modules.debconf import get_selections
    selections = get_selections(module, pkg)

    assert selections == expected_selections
    module.get_bin_path.assert_called_once_with('debconf-show', True)
    module.run_command.assert_called_once_with('/usr/bin/debconf-show some-package')

def test_get_selections_failure(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/usr/bin/debconf-show'
    module.run_command.return_value = (1, '', 'error message')

    pkg = 'some-package'

    from ansible.modules.debconf import get_selections

    def fail_json(**kwargs):
        raise Exception(kwargs['msg'])

    module.fail_json.side_effect = fail_json

    with pytest.raises(Exception) as excinfo:
        get_selections(module, pkg)

    assert str(excinfo.value) == 'error message'
    module.get_bin_path.assert_called_once_with('debconf-show', True)
    module.run_command.assert_called_once_with('/usr/bin/debconf-show some-package')
