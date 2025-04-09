# file: lib/ansible/plugins/action/pause.py:298-304
# asked: {"lines": [299, 300, 301, 302, 303, 304], "branches": [[299, 300], [301, 302], [301, 303], [303, 299], [303, 304]]}
# gained: {"lines": [299, 300, 301, 302, 303, 304], "branches": [[299, 300], [301, 302], [301, 303], [303, 299], [303, 304]]}

import pytest
from ansible.plugins.action.pause import ActionModule
from io import BytesIO
from unittest.mock import Mock

@pytest.fixture
def action_module():
    task = Mock()
    connection = Mock()
    play_context = Mock()
    loader = Mock()
    templar = Mock()
    shared_loader_obj = Mock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_c_or_a_returns_true_on_c(action_module):
    stdin = BytesIO(b'c')
    result = action_module._c_or_a(stdin)
    assert result is True

def test_c_or_a_returns_false_on_a(action_module):
    stdin = BytesIO(b'a')
    result = action_module._c_or_a(stdin)
    assert result is False

def test_c_or_a_ignores_other_keys(action_module):
    stdin = BytesIO(b'x' * 10 + b'c')
    result = action_module._c_or_a(stdin)
    assert result is True

def test_c_or_a_case_insensitivity(action_module):
    stdin = BytesIO(b'C')
    result = action_module._c_or_a(stdin)
    assert result is True

    stdin = BytesIO(b'A')
    result = action_module._c_or_a(stdin)
    assert result is False
