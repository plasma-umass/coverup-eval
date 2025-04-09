# file lib/ansible/template/vars.py:108-122
# lines [113, 114, 119, 120, 122]
# branches ['113->114', '113->119']

import pytest
from ansible.template.vars import AnsibleJ2Vars
from collections.abc import Mapping

class TestAnsibleJ2Vars:
    def test_add_locals_none(self, mocker):
        mock_templar = mocker.Mock()
        mock_globals = mocker.Mock()
        ansible_vars = AnsibleJ2Vars(mock_templar, mock_globals)
        result = ansible_vars.add_locals(None)
        assert result is ansible_vars

    def test_add_locals_with_data(self, mocker):
        mock_templar = mocker.Mock()
        mock_globals = mocker.Mock()
        ansible_vars = AnsibleJ2Vars(mock_templar, mock_globals)
        ansible_vars._locals = {'existing_key': 'existing_value'}
        
        new_locals = {'new_key': 'new_value'}
        result = ansible_vars.add_locals(new_locals)
        
        assert isinstance(result, AnsibleJ2Vars)
        assert result._locals['existing_key'] == 'existing_value'
        assert result._locals['new_key'] == 'new_value'
        assert result._templar is mock_templar
        assert result._globals is mock_globals
