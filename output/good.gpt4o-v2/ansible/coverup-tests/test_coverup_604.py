# file: lib/ansible/cli/arguments/option_helpers.py:81-84
# asked: {"lines": [81, 82, 83, 84], "branches": [[82, 83], [82, 84]]}
# gained: {"lines": [81, 82, 83, 84], "branches": [[82, 83], [82, 84]]}

import pytest

class Namespace:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

def test_ensure_value_sets_value():
    from ansible.cli.arguments.option_helpers import ensure_value

    namespace = Namespace()
    ensure_value(namespace, 'test_attr', 'test_value')
    assert namespace.test_attr == 'test_value'

def test_ensure_value_does_not_override():
    from ansible.cli.arguments.option_helpers import ensure_value

    namespace = Namespace(test_attr='existing_value')
    ensure_value(namespace, 'test_attr', 'new_value')
    assert namespace.test_attr == 'existing_value'
