# file lib/ansible/modules/debconf.py:129-142
# lines [129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 142]
# branches ['132->133', '132->135', '135->136', '135->140', '136->137', '136->138', '138->139', '138->140']

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.get_bin_path.return_value = '/usr/bin/debconf-set-selections'
    mock_module.run_command.return_value = (0, 'output', 'error')
    return mock_module

def test_set_selection_boolean_true(mock_module):
    from ansible.modules.debconf import set_selection
    set_selection(mock_module, 'package', 'question', 'boolean', 'True', False)
    mock_module.run_command.assert_called_once_with(
        ['/usr/bin/debconf-set-selections'], data='package question boolean true'
    )

def test_set_selection_boolean_false(mock_module):
    from ansible.modules.debconf import set_selection
    set_selection(mock_module, 'package', 'question', 'boolean', 'False', False)
    mock_module.run_command.assert_called_once_with(
        ['/usr/bin/debconf-set-selections'], data='package question boolean false'
    )

def test_set_selection_unseen(mock_module):
    from ansible.modules.debconf import set_selection
    set_selection(mock_module, 'package', 'question', 'string', 'value', True)
    mock_module.run_command.assert_called_once_with(
        ['/usr/bin/debconf-set-selections', '-u'], data='package question string value'
    )
