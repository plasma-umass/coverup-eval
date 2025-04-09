# file: lib/ansible/cli/doc.py:506-513
# asked: {"lines": [507, 508, 509, 510, 513], "branches": [[509, 510], [509, 513]]}
# gained: {"lines": [507, 508, 509, 510, 513], "branches": [[509, 510], [509, 513]]}

import pytest
from unittest.mock import patch
from ansible.cli.doc import DocCLI

@pytest.fixture
def doc_cli_instance():
    args = ['dummy_arg']
    return DocCLI(args)

def test_display_role_doc(doc_cli_instance):
    role_json = {
        'role1': {'key1': 'value1'},
        'role2': {'key2': 'value2'}
    }

    with patch.object(DocCLI, 'get_role_man_text', return_value=['role_text']) as mock_get_role_man_text, \
         patch.object(DocCLI, 'pager') as mock_pager:
        
        doc_cli_instance._display_role_doc(role_json)
        
        mock_get_role_man_text.assert_any_call('role1', {'key1': 'value1'})
        mock_get_role_man_text.assert_any_call('role2', {'key2': 'value2'})
        mock_pager.assert_called_once_with("role_text\nrole_text")
