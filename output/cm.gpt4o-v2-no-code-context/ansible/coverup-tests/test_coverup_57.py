# file: lib/ansible/cli/doc.py:473-504
# asked: {"lines": [473, 478, 479, 480, 481, 482, 484, 485, 487, 488, 489, 490, 492, 493, 495, 496, 497, 498, 499, 500, 501, 504], "branches": [[480, 481], [480, 484], [481, 480], [481, 482], [487, 488], [487, 489], [489, 490], [489, 492], [495, 496], [495, 504], [496, 495], [496, 497], [497, 498], [497, 499]]}
# gained: {"lines": [473, 478, 479, 480, 481, 482, 484, 485, 487, 488, 489, 490, 492, 493, 495, 496, 497, 499, 500, 501, 504], "branches": [[480, 481], [480, 484], [481, 480], [481, 482], [487, 488], [489, 490], [495, 496], [495, 504], [496, 495], [496, 497], [497, 499]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_display(monkeypatch):
    mock_display = MagicMock()
    mock_display.columns = 80
    monkeypatch.setattr('ansible.cli.doc.display', mock_display)
    return mock_display

@pytest.fixture
def mock_pager(monkeypatch):
    mock_pager = MagicMock()
    monkeypatch.setattr(DocCLI, 'pager', mock_pager)
    return mock_pager

@pytest.fixture
def doc_cli():
    args = MagicMock()
    return DocCLI(args)

def test_display_available_roles(mock_display, mock_pager, doc_cli):
    list_json = {
        'role1': {
            'entry_points': {
                'ep1': 'This is a description for entry point 1',
                'ep2': 'This is a description for entry point 2'
            }
        },
        'role2': {
            'entry_points': {
                'ep3': 'This is a description for entry point 3'
            }
        }
    }

    doc_cli._display_available_roles(list_json)

    assert mock_pager.called
    output = mock_pager.call_args[0][0]
    assert 'role1' in output
    assert 'ep1' in output
    assert 'ep2' in output
    assert 'role2' in output
    assert 'ep3' in output
    assert 'This is a description for entry point 1' in output
    assert 'This is a description for entry point 2' in output
    assert 'This is a description for entry point 3' in output
