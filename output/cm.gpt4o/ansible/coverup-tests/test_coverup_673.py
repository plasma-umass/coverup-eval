# file lib/ansible/cli/doc.py:358-361
# lines [358, 360, 361]
# branches []

import pytest
from unittest.mock import patch
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_cli(mocker):
    mocker.patch('ansible.cli.doc.CLI.__init__', return_value=None)
    mocker.patch('ansible.cli.doc.RoleMixin', autospec=True)

def test_doccli_init(mock_cli):
    args = ['arg1', 'arg2']
    doc_cli = DocCLI(args)
    
    assert doc_cli.plugin_list == set()
    assert isinstance(doc_cli, DocCLI)
