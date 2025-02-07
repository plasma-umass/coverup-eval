# file: lib/ansible/cli/doc.py:432-437
# asked: {"lines": [432, 433, 435, 437], "branches": []}
# gained: {"lines": [432, 433, 435, 437], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.doc import DocCLI
from ansible.utils.display import Display

@pytest.fixture
def mock_display(monkeypatch):
    display = MagicMock(spec=Display)
    monkeypatch.setattr('ansible.cli.doc.display', display)
    return display

def test_post_process_args(mock_display):
    class MockCLI(DocCLI):
        def __init__(self, args):
            super(MockCLI, self).__init__(args)
            self.parser = MagicMock()
            self.parser.prog = 'ansible-doc'

    options = MagicMock()
    options.verbosity = 3

    cli = MockCLI(args=['test'])
    processed_options = cli.post_process_args(options)

    assert processed_options == options
    assert mock_display.verbosity == 3
