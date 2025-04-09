# file lib/ansible/cli/arguments/option_helpers.py:81-84
# lines [81, 82, 83, 84]
# branches ['82->83', '82->84']

import pytest
from ansible.cli.arguments.option_helpers import ensure_value

class MockNamespace:
    pass

@pytest.fixture
def mock_namespace():
    return MockNamespace()

def test_ensure_value_new_attr(mock_namespace):
    # Test that ensure_value sets the attribute if it doesn't exist
    attr_name = 'new_attr'
    attr_value = 'new_value'
    result = ensure_value(mock_namespace, attr_name, attr_value)
    assert getattr(mock_namespace, attr_name) == attr_value
    assert result == attr_value

def test_ensure_value_existing_attr(mock_namespace):
    # Test that ensure_value does not change the attribute if it exists
    attr_name = 'existing_attr'
    existing_value = 'existing_value'
    new_value = 'new_value'
    setattr(mock_namespace, attr_name, existing_value)
    result = ensure_value(mock_namespace, attr_name, new_value)
    assert getattr(mock_namespace, attr_name) == existing_value
    assert result == existing_value
