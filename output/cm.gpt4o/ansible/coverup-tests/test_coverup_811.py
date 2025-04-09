# file lib/ansible/cli/playbook.py:28-31
# lines [28, 29]
# branches []

import pytest
from unittest.mock import patch
from ansible.cli.playbook import PlaybookCLI

@pytest.fixture
def mock_cli(mocker):
    mocker.patch('ansible.cli.playbook.CLI.__init__', return_value=None)
    return PlaybookCLI()

def test_playbook_cli_initialization(mock_cli):
    assert isinstance(mock_cli, PlaybookCLI)
    expected_doc = ''' the tool to run *Ansible playbooks*, which are a configuration and multinode deployment system.
    See the project home page (https://docs.ansible.com) for more information. '''
    assert mock_cli.__doc__.replace(" ", "").replace("\n", "") == expected_doc.replace(" ", "").replace("\n", "")
