# file lib/ansible/plugins/inventory/generator.py:103-105
# lines [104, 105]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.inventory.generator import InventoryModule

@pytest.fixture
def mock_templar(mocker):
    templar_mock = MagicMock()
    mocker.patch.object(InventoryModule, 'templar', templar_mock, create=True)
    return templar_mock

def test_template_executes_missing_lines(mock_templar):
    # Arrange
    inventory_module = InventoryModule()
    pattern = "some_pattern"
    variables = {"key": "value"}

    # Act
    result = inventory_module.template(pattern, variables)

    # Assert
    mock_templar.available_variables = variables
    mock_templar.do_template.assert_called_once_with(pattern)
    assert result == mock_templar.do_template.return_value
