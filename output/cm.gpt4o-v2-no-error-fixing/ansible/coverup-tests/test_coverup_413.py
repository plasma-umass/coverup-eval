# file: lib/ansible/plugins/become/su.py:136-144
# asked: {"lines": [136, 139, 140, 142, 143, 144], "branches": []}
# gained: {"lines": [136, 139, 140, 142, 143, 144], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.become.su import BecomeModule

@pytest.fixture
def become_module():
    return BecomeModule()

def test_check_password_prompt_with_localization(become_module):
    mock_get_option = MagicMock(return_value=['password'])
    with patch.object(become_module, 'get_option', mock_get_option):
        b_output = b"password: "
        assert become_module.check_password_prompt(b_output) == True

def test_check_password_prompt_without_localization(become_module):
    mock_get_option = MagicMock(return_value=None)
    become_module.SU_PROMPT_LOCALIZATIONS = ['password']
    with patch.object(become_module, 'get_option', mock_get_option):
        b_output = b"password: "
        assert become_module.check_password_prompt(b_output) == True

def test_check_password_prompt_no_match(become_module):
    mock_get_option = MagicMock(return_value=['password'])
    with patch.object(become_module, 'get_option', mock_get_option):
        b_output = b"no match"
        assert become_module.check_password_prompt(b_output) == False
