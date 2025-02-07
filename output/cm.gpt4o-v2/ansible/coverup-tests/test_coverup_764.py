# file: lib/ansible/cli/doc.py:997-999
# asked: {"lines": [997, 998, 999], "branches": []}
# gained: {"lines": [997, 998, 999], "branches": []}

import pytest
from ansible.cli.doc import DocCLI
import yaml
from ansible.parsing.yaml.dumper import AnsibleDumper

def test_dump_yaml(monkeypatch):
    # Mock the tty_ify method to just return the input text
    def mock_tty_ify(text):
        return text

    monkeypatch.setattr(DocCLI, 'tty_ify', mock_tty_ify)

    struct = {'key': 'value'}
    indent = '  '
    expected_output = '  key: value\n'

    result = DocCLI._dump_yaml(struct, indent)
    
    assert result.strip() == expected_output.strip()
