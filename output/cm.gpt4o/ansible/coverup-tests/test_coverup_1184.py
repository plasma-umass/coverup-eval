# file lib/ansible/cli/doc.py:506-513
# lines [507, 508, 509, 510, 513]
# branches ['509->510', '509->513']

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_pager(mocker):
    return mocker.patch('ansible.cli.doc.DocCLI.pager')

def test_display_role_doc(mock_pager):
    args = MagicMock()
    cli = DocCLI(args)
    role_json = {
        'role1': {'key1': 'value1'},
        'role2': {'key2': 'value2'}
    }

    with patch.object(cli, 'get_role_man_text', side_effect=lambda role, data: [f"Documentation for {role}"]):
        cli._display_role_doc(role_json)

    mock_pager.assert_called_once_with("Documentation for role1\nDocumentation for role2")
