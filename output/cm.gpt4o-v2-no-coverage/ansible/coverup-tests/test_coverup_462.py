# file: lib/ansible/cli/arguments/option_helpers.py:317-337
# asked: {"lines": [317, 324, 327, 328, 329, 330, 331, 332, 333, 335, 337], "branches": []}
# gained: {"lines": [317, 324, 327, 328, 329, 330, 331, 332, 333, 335, 337], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.arguments.option_helpers import add_runas_options, add_runas_prompt_options

@pytest.fixture
def mock_parser():
    return MagicMock()

def test_add_runas_options(mock_parser):
    add_runas_options(mock_parser)
    
    # Check if the argument groups were added
    assert mock_parser.add_argument_group.call_count == 3
    
    # Check if the correct arguments were added to the runas_group
    runas_group = mock_parser.add_argument_group.call_args_list[0][0][0]
    assert runas_group == "Privilege Escalation Options"
    
    runas_group_args = mock_parser.add_argument_group.call_args_list[0][0][1]
    assert "control how and which user you become as on target hosts" in runas_group_args
    
    # Check if the correct arguments were added to the parser
    args = [call[1] for call in mock_parser.add_argument_group().add_argument.call_args_list]
    assert any(arg['dest'] == 'become' for arg in args)
    assert any(arg['dest'] == 'become_method' for arg in args)
    assert any(arg['dest'] == 'become_user' for arg in args)

def test_add_runas_prompt_options(mock_parser):
    add_runas_prompt_options(mock_parser)
    
    # Check if the argument groups were added
    assert mock_parser.add_argument_group.call_count == 1
    
    # Check if the correct arguments were added to the runas_pass_group
    runas_pass_group = mock_parser.add_mutually_exclusive_group()
    args = [call[1] for call in runas_pass_group.add_argument.call_args_list]
    assert any(arg['dest'] == 'become_ask_pass' for arg in args)
    assert any(arg['dest'] == 'become_password_file' for arg in args)
