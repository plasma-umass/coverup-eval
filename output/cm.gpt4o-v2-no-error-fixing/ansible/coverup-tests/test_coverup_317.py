# file: lib/ansible/template/vars.py:108-122
# asked: {"lines": [108, 113, 114, 119, 120, 122], "branches": [[113, 114], [113, 119]]}
# gained: {"lines": [108, 113, 114, 119, 120, 122], "branches": [[113, 114], [113, 119]]}

import pytest
from ansible.template.vars import AnsibleJ2Vars

class MockTemplar:
    pass

class TestAnsibleJ2Vars:
    def setup_method(self):
        self.templar = MockTemplar()
        self.globals = {'global_var': 'value'}
        self.locals = {'local_var': 'value'}
        self.ansible_j2_vars = AnsibleJ2Vars(self.templar, self.globals, locals=self.locals)

    def test_add_locals_with_none(self):
        result = self.ansible_j2_vars.add_locals(None)
        assert result is self.ansible_j2_vars

    def test_add_locals_with_new_locals(self):
        new_locals = {'new_local_var': 'new_value'}
        result = self.ansible_j2_vars.add_locals(new_locals)
        assert result is not self.ansible_j2_vars
        assert isinstance(result, AnsibleJ2Vars)
        assert result._locals['new_local_var'] == 'new_value'
        assert result._locals['local_var'] == 'value'
        assert result._globals == self.globals
        assert result._templar == self.templar
