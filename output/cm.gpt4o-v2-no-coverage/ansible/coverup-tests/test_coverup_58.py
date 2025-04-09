# file: lib/ansible/cli/doc.py:473-504
# asked: {"lines": [473, 478, 479, 480, 481, 482, 484, 485, 487, 488, 489, 490, 492, 493, 495, 496, 497, 498, 499, 500, 501, 504], "branches": [[480, 481], [480, 484], [481, 480], [481, 482], [487, 488], [487, 489], [489, 490], [489, 492], [495, 496], [495, 504], [496, 495], [496, 497], [497, 498], [497, 499]]}
# gained: {"lines": [473, 478, 479, 480, 481, 482, 484, 485, 487, 488, 489, 490, 492, 493, 495, 496, 497, 499, 500, 501, 504], "branches": [[480, 481], [480, 484], [481, 480], [481, 482], [487, 488], [489, 490], [495, 496], [495, 504], [496, 495], [496, 497], [497, 499]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_display_columns(monkeypatch):
    mock_display = MagicMock()
    mock_display.columns = 80
    monkeypatch.setattr('ansible.cli.doc.display', mock_display)
    return mock_display

def test_display_available_roles(mock_display_columns):
    list_json = {
        'role1': {
            'entry_points': {
                'ep1': 'description1',
                'ep2': 'description2'
            }
        },
        'role2': {
            'entry_points': {
                'ep3': 'description3',
                'ep4': 'description4'
            }
        }
    }

    with patch.object(DocCLI, 'pager', return_value=None) as mock_pager:
        doc_cli = DocCLI(args=['test'])
        doc_cli._display_available_roles(list_json)
        
        expected_text = [
            "role1 ep1 description1",
            "role1 ep2 description2",
            "role2 ep3 description3",
            "role2 ep4 description4"
        ]
        mock_pager.assert_called_once_with("\n".join(expected_text))
