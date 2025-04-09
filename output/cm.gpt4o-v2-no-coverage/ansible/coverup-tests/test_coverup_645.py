# file: lib/ansible/plugins/become/su.py:136-144
# asked: {"lines": [136, 139, 140, 142, 143, 144], "branches": []}
# gained: {"lines": [136, 139, 140, 142, 143, 144], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.become.su import BecomeModule

@pytest.fixture
def become_module():
    module = BecomeModule()
    module.get_option = MagicMock()
    return module

def test_check_password_prompt_with_prompt_l10n(become_module):
    become_module.get_option.return_value = ['Password']
    b_output = b"Password: "
    assert become_module.check_password_prompt(b_output) == True

def test_check_password_prompt_with_SU_PROMPT_LOCALIZATIONS(become_module):
    become_module.get_option.return_value = None
    b_output = b"Password: "
    assert become_module.check_password_prompt(b_output) == True

def test_check_password_prompt_with_incorrect_prompt(become_module):
    become_module.get_option.return_value = ['Password']
    b_output = b"Incorrect: "
    assert become_module.check_password_prompt(b_output) == False

def test_check_password_prompt_with_unicode_colon(become_module):
    become_module.get_option.return_value = ['Password']
    b_output = "Password\uff1a ".encode('utf-8')
    assert become_module.check_password_prompt(b_output) == True
