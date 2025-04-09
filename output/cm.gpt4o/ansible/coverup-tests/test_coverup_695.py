# file lib/ansible/cli/doc.py:997-999
# lines [997, 998, 999]
# branches []

import pytest
from unittest.mock import patch
import yaml
from ansible.cli.doc import DocCLI
from ansible.utils.display import Display

class AnsibleDumper(yaml.SafeDumper):
    pass

def test_dump_yaml(mocker):
    struct = {'key': 'value'}
    indent = '  '

    # Mock the tty_ify method to just return its input for simplicity
    mocker.patch.object(DocCLI, 'tty_ify', side_effect=lambda x: x)

    result = DocCLI._dump_yaml(struct, indent)

    expected_yaml = yaml.dump(struct, default_flow_style=False, Dumper=AnsibleDumper)
    expected_result = '\n'.join([indent + line for line in expected_yaml.split('\n')])

    assert result == expected_result
