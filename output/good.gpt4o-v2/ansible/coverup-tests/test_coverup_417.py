# file: lib/ansible/playbook/conditional.py:51-60
# asked: {"lines": [51, 55, 56, 57, 59, 60], "branches": [[55, 56], [55, 60], [56, 57], [56, 59]]}
# gained: {"lines": [51, 55, 56, 57, 59, 60], "branches": [[55, 56], [55, 60], [56, 57], [56, 59]]}

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.conditional import Conditional

def test_conditional_init_with_loader():
    loader = object()
    cond = Conditional(loader=loader)
    assert cond._loader == loader

def test_conditional_init_without_loader():
    with pytest.raises(AnsibleError, match="a loader must be specified when using Conditional\\(\\) directly"):
        Conditional(loader=None)

def test_conditional_init_with_existing_loader(monkeypatch):
    class MockConditional(Conditional):
        def __init__(self):
            self._loader = "existing_loader"
            super(MockConditional, self).__init__()

    cond = MockConditional()
    assert cond._loader == "existing_loader"
