# file lib/ansible/cli/arguments/option_helpers.py:293-298
# lines [293, 295, 296, 297, 298]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.constants import DEFAULT_FORCE_HANDLERS
from ansible.cli.arguments.option_helpers import add_meta_options

class MockParser:
    def __init__(self):
        self.arguments = []

    def add_argument(self, *args, **kwargs):
        self.arguments.append((args, kwargs))

@pytest.fixture
def mock_parser():
    return MockParser()

def test_add_meta_options(mock_parser):
    add_meta_options(mock_parser)
    
    # Check if '--force-handlers' is in the added arguments
    force_handlers_arg = next((arg for arg in mock_parser.arguments if '--force-handlers' in arg[0]), None)
    assert force_handlers_arg is not None
    assert force_handlers_arg[1]['default'] == DEFAULT_FORCE_HANDLERS
    assert force_handlers_arg[1]['dest'] == 'force_handlers'
    assert force_handlers_arg[1]['action'] == 'store_true'
    assert 'help' in force_handlers_arg[1]

    # Check if '--flush-cache' is in the added arguments
    flush_cache_arg = next((arg for arg in mock_parser.arguments if '--flush-cache' in arg[0]), None)
    assert flush_cache_arg is not None
    assert flush_cache_arg[1]['dest'] == 'flush_cache'
    assert flush_cache_arg[1]['action'] == 'store_true'
    assert 'help' in flush_cache_arg[1]
