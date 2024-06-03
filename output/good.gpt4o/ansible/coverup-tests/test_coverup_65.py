# file lib/ansible/cli/doc.py:473-504
# lines [473, 478, 479, 480, 481, 482, 484, 485, 487, 488, 489, 490, 492, 493, 495, 496, 497, 498, 499, 500, 501, 504]
# branches ['480->481', '480->484', '481->480', '481->482', '487->488', '487->489', '489->490', '489->492', '495->496', '495->504', '496->495', '496->497', '497->498', '497->499']

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_display():
    with patch('ansible.cli.doc.display') as mock_display:
        mock_display.columns = 80
        yield mock_display

@pytest.fixture
def mock_pager():
    with patch('ansible.cli.doc.DocCLI.pager') as mock_pager:
        yield mock_pager

def test_display_available_roles(mock_display, mock_pager):
    list_json = {
        'role1': {
            'entry_points': {
                'main': 'This is a description of the main entry point for role1.',
                'extra': 'Extra entry point for role1.'
            }
        },
        'role2': {
            'entry_points': {
                'main': 'Main entry point for role2.'
            }
        }
    }

    cli = DocCLI(args=['dummy_arg'])
    cli._display_available_roles(list_json)

    expected_output = [
        "role1 main  This is a description of the main entry point for role1.",
        "role1 extra Extra entry point for role1.",
        "role2 main  Main entry point for role2."
    ]

    mock_pager.assert_called_once_with("\n".join(expected_output))
