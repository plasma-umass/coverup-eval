# file lib/ansible/cli/inventory.py:100-122
# lines [100, 101, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 117, 118, 120, 122]
# branches ['108->109', '108->111', '109->108', '109->110', '111->112', '111->113', '113->114', '113->117', '117->118', '117->120']

import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.errors import AnsibleOptionsError
from ansible.utils.display import Display

# Mock the Display class to prevent any real output during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch('ansible.utils.display.Display')

# Create a mock options class to simulate command line options
class MockOptions:
    def __init__(self, verbosity=0, list=False, host=False, graph=False, args=None):
        self.verbosity = verbosity
        self.list = list
        self.host = host
        self.graph = graph
        self.args = args
        self.pattern = None

# Fixture to create an InventoryCLI instance with a mock parser
@pytest.fixture
def inventory_cli(mocker):
    mocker.patch('ansible.cli.inventory.InventoryCLI.parse', return_value=MockOptions())
    cli = InventoryCLI(['ansible-inventory'])
    cli.parser = mocker.MagicMock()
    cli.parser.prog = 'ansible-inventory'
    return cli

# Test function to check the error when no action is selected
def test_no_action_selected(inventory_cli):
    options = MockOptions()
    with pytest.raises(AnsibleOptionsError) as excinfo:
        inventory_cli.post_process_args(options)
    assert "No action selected" in str(excinfo.value)

# Test function to check the error when conflicting options are used
def test_conflicting_options_used(inventory_cli):
    options = MockOptions(list=True, host=True)
    with pytest.raises(AnsibleOptionsError) as excinfo:
        inventory_cli.post_process_args(options)
    assert "Conflicting options used" in str(excinfo.value)

# Test function to check that the default pattern is set when no args are provided
def test_default_pattern_set(inventory_cli):
    options = MockOptions(list=True)
    processed_options = inventory_cli.post_process_args(options)
    assert processed_options.pattern == 'all'

# Test function to check that a custom pattern is set when args are provided
def test_custom_pattern_set(inventory_cli):
    options = MockOptions(list=True, args='custom_pattern')
    processed_options = inventory_cli.post_process_args(options)
    assert processed_options.pattern == 'custom_pattern'
