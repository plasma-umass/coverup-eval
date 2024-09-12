# file: lib/ansible/cli/doc.py:358-361
# asked: {"lines": [358, 360, 361], "branches": []}
# gained: {"lines": [358, 360, 361], "branches": []}

import pytest
from ansible.cli.doc import DocCLI

def test_doccli_init():
    args = ['arg1', 'arg2']
    doc_cli = DocCLI(args)
    
    assert doc_cli.args == args
    assert doc_cli.plugin_list == set()
