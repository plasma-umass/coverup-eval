# file: lib/ansible/cli/doc.py:473-504
# asked: {"lines": [498], "branches": [[487, 489], [489, 492], [497, 498]]}
# gained: {"lines": [498], "branches": [[487, 489], [489, 492], [497, 498]]}

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

@pytest.fixture
def cli():
    return DocCLI(args=['test'])

def test_display_available_roles_empty(cli, mock_display, mock_pager):
    list_json = {}
    cli._display_available_roles(list_json)
    mock_pager.assert_called_once_with('')

def test_display_available_roles_single_role_single_entry_point(cli, mock_display, mock_pager):
    list_json = {
        'role1': {
            'entry_points': {
                'ep1': 'description1'
            }
        }
    }
    cli._display_available_roles(list_json)
    expected_output = 'role1 ep1 description1'
    mock_pager.assert_called_once_with(expected_output)

def test_display_available_roles_multiple_roles_multiple_entry_points(cli, mock_display, mock_pager):
    list_json = {
        'role1': {
            'entry_points': {
                'ep1': 'description1',
                'ep2': 'description2'
            }
        },
        'role2': {
            'entry_points': {
                'ep3': 'description3'
            }
        }
    }
    cli._display_available_roles(list_json)
    expected_output = 'role1 ep1 description1\nrole1 ep2 description2\nrole2 ep3 description3'
    mock_pager.assert_called_once_with(expected_output)

def test_display_available_roles_long_description(cli, mock_display, mock_pager):
    long_description = 'a' * 100
    list_json = {
        'role1': {
            'entry_points': {
                'ep1': long_description
            }
        }
    }
    cli._display_available_roles(list_json)
    truncated_description = long_description[:mock_display.columns - len('role1') - len('ep1') - 5] + '...'
    expected_output = f'role1 ep1 {truncated_description}'
    mock_pager.assert_called_once_with(expected_output)
