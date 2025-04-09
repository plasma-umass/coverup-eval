# file lib/ansible/cli/doc.py:358-361
# lines [358, 360, 361]
# branches []

import pytest
from ansible.cli.doc import DocCLI
from unittest.mock import MagicMock

# Assuming the existence of a fixture that provides command line arguments
@pytest.fixture
def args():
    return ['ansible-doc', '--version']

# Test function to cover the __init__ method of DocCLI
def test_doc_cli_init(mocker, args):
    mocker.patch('ansible.cli.doc.CLI.__init__', return_value=None)
    mocker.patch('ansible.cli.doc.RoleMixin', create=True)

    doc_cli = DocCLI(args)

    # Assertions to verify postconditions
    assert isinstance(doc_cli, DocCLI)
    assert doc_cli.plugin_list == set()

    # Cleanup is handled by pytest's fixture scope and mocker's automatic patching
