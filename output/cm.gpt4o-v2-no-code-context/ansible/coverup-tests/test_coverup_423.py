# file: lib/ansible/template/vars.py:108-122
# asked: {"lines": [108, 113, 114, 119, 120, 122], "branches": [[113, 114], [113, 119]]}
# gained: {"lines": [108, 113, 114, 119, 120, 122], "branches": [[113, 114], [113, 119]]}

import pytest
from ansible.template.vars import AnsibleJ2Vars
from collections.abc import Mapping

class TestAnsibleJ2Vars:
    @pytest.fixture
    def ansible_j2_vars(self):
        class MockTemplar:
            pass

        templar = MockTemplar()
        globals = {}
        locals = {}
        return AnsibleJ2Vars(templar, globals, locals)

    def test_add_locals_none(self, ansible_j2_vars):
        result = ansible_j2_vars.add_locals(None)
        assert result is ansible_j2_vars

    def test_add_locals_with_data(self, ansible_j2_vars):
        new_locals = {'key': 'value'}
        result = ansible_j2_vars.add_locals(new_locals)
        assert isinstance(result, AnsibleJ2Vars)
        assert result._locals['key'] == 'value'
        assert result._templar is ansible_j2_vars._templar
        assert result._globals is ansible_j2_vars._globals
