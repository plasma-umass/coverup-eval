# file: lib/ansible/cli/doc.py:439-471
# asked: {"lines": [442, 443, 444, 447, 449, 450, 451, 454, 455, 456, 458, 459, 461, 462, 464, 466, 467, 468, 471], "branches": [[447, 449], [447, 454], [449, 450], [449, 471], [455, 456], [455, 471], [458, 459], [458, 461], [461, 462], [461, 464], [466, 455], [466, 467]]}
# gained: {"lines": [442, 443, 444, 447, 449, 450, 451, 454, 455, 456, 458, 461, 462, 464, 466, 467, 468, 471], "branches": [[447, 449], [447, 454], [449, 450], [449, 471], [455, 456], [455, 471], [458, 461], [461, 462], [461, 464], [466, 455], [466, 467]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_display_columns(monkeypatch):
    mock_display = MagicMock()
    mock_display.columns = 80
    monkeypatch.setattr('ansible.cli.doc.display', mock_display)
    return mock_display

@pytest.fixture
def mock_context_cliargs(monkeypatch):
    mock_context = MagicMock()
    mock_context.CLIARGS = {'list_files': False}
    monkeypatch.setattr('ansible.cli.doc.context', mock_context)
    return mock_context

@pytest.fixture
def mock_pager(monkeypatch):
    mock_pager = MagicMock()
    monkeypatch.setattr(DocCLI, 'pager', mock_pager)
    return mock_pager

@pytest.fixture
def mock_tty_ify(monkeypatch):
    mock_tty_ify = MagicMock(side_effect=lambda x: x)
    monkeypatch.setattr(DocCLI, 'tty_ify', mock_tty_ify)
    return mock_tty_ify

def test_display_plugin_list_files(mock_display_columns, mock_context_cliargs, mock_pager):
    mock_context_cliargs.CLIARGS['list_files'] = True
    doc_cli = DocCLI(args=['test'])
    doc_cli.plugin_list = ['plugin1', 'plugin2']
    results = {'plugin1': 'filename1', 'plugin2': 'filename2'}
    
    doc_cli.display_plugin_list(results)
    
    assert mock_pager.called
    output = "\n".join(mock_pager.call_args[0][0].split("\n"))
    assert "plugin1" in output
    assert "filename1" in output
    assert "plugin2" in output
    assert "filename2" in output

def test_display_plugin_list_descriptions(mock_display_columns, mock_context_cliargs, mock_pager, mock_tty_ify):
    doc_cli = DocCLI(args=['test'])
    doc_cli.plugin_list = ['plugin1', '_plugin2']
    results = {'plugin1': 'description1', '_plugin2': 'description2'}
    
    doc_cli.display_plugin_list(results)
    
    assert mock_tty_ify.called
    assert mock_pager.called
    output = "\n".join(mock_pager.call_args[0][0].split("\n"))
    assert "plugin1" in output
    assert "description1" in output
    assert "plugin2" in output
    assert "description2" in output
    assert "DEPRECATED:" in output
