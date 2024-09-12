# file: lib/ansible/cli/doc.py:439-471
# asked: {"lines": [459], "branches": [[458, 459]]}
# gained: {"lines": [459], "branches": [[458, 459]]}

import pytest
from ansible.cli.doc import DocCLI
from ansible import context

@pytest.fixture
def mock_display_columns(monkeypatch):
    class MockDisplay:
        columns = 80
    monkeypatch.setattr('ansible.cli.doc.display', MockDisplay)

@pytest.fixture
def mock_context_cliargs(monkeypatch):
    monkeypatch.setattr(context, 'CLIARGS', {'list_files': False})

@pytest.fixture
def mock_pager(monkeypatch):
    def mock_pager_function(text):
        mock_pager_function.output = text
    monkeypatch.setattr(DocCLI, 'pager', mock_pager_function)
    return mock_pager_function

def test_display_plugin_list_truncates_description(mock_display_columns, mock_context_cliargs, mock_pager):
    doc_cli = DocCLI(args=['test'])
    doc_cli.plugin_list = ['plugin1', 'plugin2']
    results = {
        'plugin1': 'A' * 100,
        'plugin2': 'Short description'
    }

    doc_cli.display_plugin_list(results)

    # Assertions to verify the truncation
    output = mock_pager.output
    assert 'plugin1' in output
    assert 'Short description' in output
    assert '...' in output
