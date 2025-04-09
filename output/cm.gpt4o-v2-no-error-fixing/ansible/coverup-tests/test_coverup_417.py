# file: lib/ansible/cli/arguments/option_helpers.py:81-84
# asked: {"lines": [81, 82, 83, 84], "branches": [[82, 83], [82, 84]]}
# gained: {"lines": [81, 82, 83, 84], "branches": [[82, 83], [82, 84]]}

import pytest

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def test_ensure_value_set_attr():
    from ansible.cli.arguments.option_helpers import ensure_value

    namespace = Namespace()
    name = 'test_attr'
    value = 'test_value'

    result = ensure_value(namespace, name, value)
    assert result == value
    assert getattr(namespace, name) == value

def test_ensure_value_existing_attr():
    from ansible.cli.arguments.option_helpers import ensure_value

    existing_value = 'existing_value'
    namespace = Namespace(test_attr=existing_value)
    name = 'test_attr'
    value = 'new_value'

    result = ensure_value(namespace, name, value)
    assert result == existing_value
    assert getattr(namespace, name) == existing_value
