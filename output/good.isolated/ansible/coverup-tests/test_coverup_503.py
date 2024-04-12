# file lib/ansible/cli/doc.py:506-513
# lines [506, 507, 508, 509, 510, 513]
# branches ['509->510', '509->513']

import pytest
from ansible.cli.doc import DocCLI
from unittest.mock import MagicMock, patch

# Assuming the existence of a valid role_json structure for testing
role_json_example = {
    'test_role': {
        'role_name': 'test_role',
        'description': 'A test role for documentation.',
        'defaults': {'var1': 'default1'},
        'examples': 'Example usage of test role',
        'return_values': 'Description of return values',
        'entry_points': {}  # Add an empty 'entry_points' to avoid KeyError
    }
}

@pytest.fixture
def mock_pager(mocker):
    return mocker.patch.object(DocCLI, 'pager')

@pytest.fixture
def mock_get_role_man_text(mocker):
    return mocker.patch.object(DocCLI, 'get_role_man_text', return_value=['Role documentation text'])

@pytest.fixture
def doc_cli_instance():
    # Provide a dummy argument to avoid ValueError
    return DocCLI(['dummy_arg'])

def test_display_role_doc(mock_pager, mock_get_role_man_text, doc_cli_instance):
    # Call the method we want to test
    doc_cli_instance._display_role_doc(role_json_example)

    # Check that the get_role_man_text method was called with the expected arguments
    mock_get_role_man_text.assert_called_once_with('test_role', role_json_example['test_role'])

    # Check that the pager method was called with the expected text
    expected_text = ['Role documentation text']
    mock_pager.assert_called_once_with("\n".join(expected_text))
