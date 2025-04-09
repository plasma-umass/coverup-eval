# file: lib/ansible/cli/doc.py:997-999
# asked: {"lines": [999], "branches": []}
# gained: {"lines": [999], "branches": []}

import pytest
from ansible.cli.doc import DocCLI
import yaml
from ansible.parsing.yaml.dumper import AnsibleDumper

def test_dump_yaml(monkeypatch):
    def mock_tty_ify(text):
        return text

    monkeypatch.setattr(DocCLI, 'tty_ify', mock_tty_ify)

    struct = {'key': 'value'}
    indent = '  '
    result = DocCLI._dump_yaml(struct, indent)
    
    expected_yaml = yaml.dump(struct, default_flow_style=False, Dumper=AnsibleDumper)
    expected_result = '\n'.join([indent + line for line in expected_yaml.split('\n')])
    
    assert result == expected_result
