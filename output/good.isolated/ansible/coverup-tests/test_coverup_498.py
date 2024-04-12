# file lib/ansible/plugins/inventory/ini.py:336-352
# lines [336, 337, 342, 343, 346, 348, 349, 351, 352]
# branches []

import pytest
import ast
from ansible.plugins.inventory.ini import InventoryModule
from ansible.module_utils._text import to_text

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_parse_value_with_valid_literal(inventory_module, mocker):
    # Mock the to_text function to ensure it is called with expected arguments
    mock_to_text = mocker.patch('ansible.plugins.inventory.ini.to_text', return_value='mocked_value')
    # Test with a valid literal that should be evaluated
    literal_value = '["a", "b", "c"]'
    result = inventory_module._parse_value(literal_value)
    # Check that the mocked to_text function was called with the evaluated literal
    mock_to_text.assert_called_once_with(ast.literal_eval(literal_value), nonstring='passthru', errors='surrogate_or_strict')
    # Check that the result is the return value of the mocked to_text function
    assert result == 'mocked_value'

def test_parse_value_with_value_error(inventory_module, mocker):
    # Mock the to_text function to ensure it is called with expected arguments
    mock_to_text = mocker.patch('ansible.plugins.inventory.ini.to_text', return_value='mocked_value')
    # Test with a string that will raise ValueError
    value_error_literal = 'unmatched "quotes'
    result = inventory_module._parse_value(value_error_literal)
    # Check that the mocked to_text function was called with the original string
    mock_to_text.assert_called_once_with(value_error_literal, nonstring='passthru', errors='surrogate_or_strict')
    # Check that the result is the return value of the mocked to_text function
    assert result == 'mocked_value'

def test_parse_value_with_syntax_error(inventory_module, mocker):
    # Mock the to_text function to ensure it is called with expected arguments
    mock_to_text = mocker.patch('ansible.plugins.inventory.ini.to_text', return_value='mocked_value')
    # Test with a string that will raise SyntaxError
    syntax_error_literal = 'invalid syntax {}'
    result = inventory_module._parse_value(syntax_error_literal)
    # Check that the mocked to_text function was called with the original string
    mock_to_text.assert_called_once_with(syntax_error_literal, nonstring='passthru', errors='surrogate_or_strict')
    # Check that the result is the return value of the mocked to_text function
    assert result == 'mocked_value'
