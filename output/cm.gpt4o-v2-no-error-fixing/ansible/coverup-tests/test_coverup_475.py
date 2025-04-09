# file: lib/ansible/plugins/inventory/generator.py:103-105
# asked: {"lines": [103, 104, 105], "branches": []}
# gained: {"lines": [103, 104, 105], "branches": []}

import pytest
from ansible.plugins.inventory.generator import InventoryModule
from unittest.mock import MagicMock

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_template_method(inventory_module, mocker):
    mock_templar = mocker.MagicMock()
    inventory_module.templar = mock_templar

    pattern = "some_pattern"
    variables = {"key": "value"}

    mock_templar.do_template.return_value = "templated_result"

    result = inventory_module.template(pattern, variables)

    mock_templar.available_variables = variables
    mock_templar.do_template.assert_called_once_with(pattern)
    assert result == "templated_result"
