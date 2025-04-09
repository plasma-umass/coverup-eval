# file: lib/ansible/cli/arguments/option_helpers.py:81-84
# asked: {"lines": [81, 82, 83, 84], "branches": [[82, 83], [82, 84]]}
# gained: {"lines": [81, 82, 83, 84], "branches": [[82, 83], [82, 84]]}

import pytest
from types import SimpleNamespace

# Assuming the function ensure_value is imported from ansible.cli.arguments.option_helpers
from ansible.cli.arguments.option_helpers import ensure_value

def test_ensure_value_sets_value():
    namespace = SimpleNamespace()
    ensure_value(namespace, 'test_attr', 'test_value')
    assert namespace.test_attr == 'test_value'

def test_ensure_value_does_not_override():
    namespace = SimpleNamespace(test_attr='existing_value')
    ensure_value(namespace, 'test_attr', 'new_value')
    assert namespace.test_attr == 'existing_value'

def test_ensure_value_returns_existing_value():
    namespace = SimpleNamespace(test_attr='existing_value')
    result = ensure_value(namespace, 'test_attr', 'new_value')
    assert result == 'existing_value'

def test_ensure_value_returns_new_value():
    namespace = SimpleNamespace()
    result = ensure_value(namespace, 'test_attr', 'new_value')
    assert result == 'new_value'
