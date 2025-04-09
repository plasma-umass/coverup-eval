# file: lib/ansible/cli/doc.py:506-513
# asked: {"lines": [506, 507, 508, 509, 510, 513], "branches": [[509, 510], [509, 513]]}
# gained: {"lines": [506, 507, 508, 509, 510, 513], "branches": [[509, 510], [509, 513]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_pager():
    with patch('ansible.cli.CLI.pager') as mock:
        yield mock

@pytest.fixture
def doc_cli_instance():
    return DocCLI(args=['dummy_arg'])

def test_display_role_doc_empty(mock_pager, doc_cli_instance):
    role_json = {}
    doc_cli_instance._display_role_doc(role_json)
    mock_pager.assert_called_once_with("")

def test_display_role_doc_single_role(mock_pager, doc_cli_instance):
    role_json = {'role1': {'path': 'some_path', 'entry_points': {}}}
    with patch.object(doc_cli_instance, 'get_role_man_text', return_value=['Role 1 Documentation']) as mock_get_role_man_text:
        doc_cli_instance._display_role_doc(role_json)
        mock_get_role_man_text.assert_called_once_with('role1', {'path': 'some_path', 'entry_points': {}})
        mock_pager.assert_called_once_with("Role 1 Documentation")

def test_display_role_doc_multiple_roles(mock_pager, doc_cli_instance):
    role_json = {
        'role1': {'path': 'some_path1', 'entry_points': {}},
        'role2': {'path': 'some_path2', 'entry_points': {}}
    }
    with patch.object(doc_cli_instance, 'get_role_man_text', side_effect=[['Role 1 Documentation'], ['Role 2 Documentation']]) as mock_get_role_man_text:
        doc_cli_instance._display_role_doc(role_json)
        assert mock_get_role_man_text.call_count == 2
        mock_get_role_man_text.assert_any_call('role1', {'path': 'some_path1', 'entry_points': {}})
        mock_get_role_man_text.assert_any_call('role2', {'path': 'some_path2', 'entry_points': {}})
        mock_pager.assert_called_once_with("Role 1 Documentation\nRole 2 Documentation")
