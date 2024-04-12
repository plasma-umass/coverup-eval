# file lib/ansible/plugins/inventory/generator.py:103-105
# lines [104, 105]
# branches []

import pytest
from ansible.plugins.inventory.generator import InventoryModule
from ansible.template import Templar
from ansible.errors import AnsibleError

# Since the original Templar class is not provided, we will create a simple mock
# that will allow us to set available_variables and capture the pattern passed to do_template.
class MockTemplar:
    def __init__(self):
        self.available_variables = None
        self.pattern = None

    def do_template(self, pattern):
        self.pattern = pattern
        return pattern

@pytest.fixture
def inventory_module(mocker):
    # Create an instance of the InventoryModule with a mocked Templar
    inventory_module = InventoryModule()
    inventory_module.templar = MockTemplar()
    return inventory_module

def test_template_method(inventory_module):
    # Define the pattern and variables to be used in the test
    pattern = "{{ inventory_hostname }}"
    variables = {'inventory_hostname': 'testhost'}

    # Call the template method which should execute lines 104-105
    result = inventory_module.template(pattern, variables)

    # Assert that the Templar's available_variables were set correctly
    assert inventory_module.templar.available_variables == variables
    # Assert that the Templar's do_template method was called with the correct pattern
    assert inventory_module.templar.pattern == pattern
    # Assert that the result of the template method is as expected
    assert result == pattern
