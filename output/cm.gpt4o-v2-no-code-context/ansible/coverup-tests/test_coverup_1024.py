# file: lib/ansible/cli/arguments/option_helpers.py:50-78
# asked: {"lines": [57, 61, 76, 77, 78], "branches": [[56, 57], [60, 61]]}
# gained: {"lines": [57, 61, 76, 77, 78], "branches": [[56, 57], [60, 61]]}

import argparse
import copy
import pytest
import re
from ansible.cli.arguments.option_helpers import PrependListAction

def ensure_value(namespace, name, default):
    if getattr(namespace, name, None) is None:
        setattr(namespace, name, default)
    return getattr(namespace, name)

def test_prepend_list_action_nargs_zero():
    with pytest.raises(ValueError, match=re.escape('nargs for append actions must be > 0; if arg strings are not supplying the value to append, the append const action may be more appropriate')):
        PrependListAction(option_strings=['--test'], dest='test', nargs=0)

def test_prepend_list_action_const_not_none_nargs_not_optional():
    with pytest.raises(ValueError, match=re.escape('nargs must be \'?\' to supply const')):
        PrependListAction(option_strings=['--test'], dest='test', nargs=argparse.ONE_OR_MORE, const='const')

def test_prepend_list_action_call(monkeypatch):
    parser = argparse.ArgumentParser()
    parser.register('action', 'prepend_list', PrependListAction)
    parser.add_argument('--test', action='prepend_list', nargs='+')

    namespace = argparse.Namespace()
    namespace.test = ['existing']

    action = PrependListAction(option_strings=['--test'], dest='test', nargs='+')
    action(parser, namespace, ['new'])

    assert namespace.test == ['new', 'existing']

@pytest.fixture
def mock_ensure_value(monkeypatch):
    def mock_ensure_value(namespace, name, default):
        if getattr(namespace, name, None) is None:
            setattr(namespace, name, default)
        return getattr(namespace, name)
    monkeypatch.setattr('ansible.cli.arguments.option_helpers.ensure_value', mock_ensure_value)

def test_prepend_list_action_call_with_mock(mock_ensure_value):
    parser = argparse.ArgumentParser()
    parser.register('action', 'prepend_list', PrependListAction)
    parser.add_argument('--test', action='prepend_list', nargs='+')

    namespace = argparse.Namespace()
    namespace.test = ['existing']

    action = PrependListAction(option_strings=['--test'], dest='test', nargs='+')
    action(parser, namespace, ['new'])

    assert namespace.test == ['new', 'existing']
