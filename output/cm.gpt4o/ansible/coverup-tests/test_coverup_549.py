# file lib/ansible/cli/arguments/option_helpers.py:81-84
# lines [81, 82, 83, 84]
# branches ['82->83', '82->84']

import pytest
from unittest.mock import Mock

def test_ensure_value():
    # Import the function from the module
    from ansible.cli.arguments.option_helpers import ensure_value

    # Create a mock namespace object
    namespace = Mock()

    # Test case where the attribute is initially None
    setattr(namespace, 'test_attr', None)
    result = ensure_value(namespace, 'test_attr', 'default_value')
    assert result == 'default_value'
    assert getattr(namespace, 'test_attr') == 'default_value'

    # Test case where the attribute is already set
    setattr(namespace, 'test_attr', 'existing_value')
    result = ensure_value(namespace, 'test_attr', 'default_value')
    assert result == 'existing_value'
    assert getattr(namespace, 'test_attr') == 'existing_value'

    # Clean up
    delattr(namespace, 'test_attr')
