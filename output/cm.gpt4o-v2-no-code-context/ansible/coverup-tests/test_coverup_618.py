# file: lib/ansible/cli/doc.py:358-361
# asked: {"lines": [358, 360, 361], "branches": []}
# gained: {"lines": [358, 360, 361], "branches": []}

import pytest
from ansible.cli.doc import DocCLI

def test_doccli_init(monkeypatch):
    args = ['arg1', 'arg2']
    
    # Mock the parent class __init__ method to avoid side effects
    def mock_init(self, args):
        self.args = args
    
    monkeypatch.setattr('ansible.cli.doc.CLI.__init__', mock_init)
    
    # Instantiate DocCLI to trigger the __init__ method
    doc_cli = DocCLI(args)
    
    # Assertions to verify the postconditions
    assert doc_cli.args == args
    assert isinstance(doc_cli.plugin_list, set)
    assert doc_cli.plugin_list == set()
