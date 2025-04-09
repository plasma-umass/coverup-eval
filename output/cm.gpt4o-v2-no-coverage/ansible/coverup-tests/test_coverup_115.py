# file: lib/ansible/cli/arguments/option_helpers.py:50-78
# asked: {"lines": [50, 51, 54, 55, 56, 57, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 75, 76, 77, 78], "branches": [[56, 57], [56, 60], [60, 61], [60, 62]]}
# gained: {"lines": [50, 51, 54, 55, 56, 57, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 75, 76, 77, 78], "branches": [[56, 57], [56, 60], [60, 61], [60, 62]]}

import pytest
import argparse
from ansible.cli.arguments.option_helpers import PrependListAction

def ensure_value(namespace, name, value):
    if getattr(namespace, name, None) is None:
        setattr(namespace, name, value)
    return getattr(namespace, name)

def test_prepend_list_action_init_nargs_zero():
    with pytest.raises(ValueError, match="nargs for append actions must be > 0; if arg strings are not supplying the value to append, the append const action may be more appropriate"):
        PrependListAction(option_strings=['--test'], dest='test', nargs=0)

def test_prepend_list_action_init_const_without_optional_nargs():
    with pytest.raises(ValueError, match="nargs must be '.*' to supply const"):
        PrependListAction(option_strings=['--test'], dest='test', const='const', nargs=argparse.ONE_OR_MORE)

def test_prepend_list_action_call(monkeypatch):
    parser = argparse.ArgumentParser()
    parser.register('action', 'prepend', PrependListAction)
    namespace = argparse.Namespace()
    
    action = PrependListAction(option_strings=['--test'], dest='test', nargs='+')
    action(parser, namespace, ['value1', 'value2'])
    
    assert namespace.test == ['value1', 'value2']
    
    action(parser, namespace, ['value3'])
    
    assert namespace.test == ['value3', 'value1', 'value2']
