# file: lib/ansible/plugins/become/su.py:136-144
# asked: {"lines": [136, 139, 140, 142, 143, 144], "branches": []}
# gained: {"lines": [136, 139, 140, 142, 143, 144], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.become.su import BecomeModule
from ansible.module_utils._text import to_bytes

@pytest.fixture
def become_module():
    module = BecomeModule()
    module.get_option = MagicMock()
    return module

def test_check_password_prompt_with_localized_prompt(become_module):
    become_module.get_option.return_value = None
    b_output = to_bytes("Password: ")
    assert become_module.check_password_prompt(b_output) == True

def test_check_password_prompt_with_custom_prompt(become_module):
    become_module.get_option.return_value = ['CustomPrompt']
    b_output = to_bytes("CustomPrompt: ")
    assert become_module.check_password_prompt(b_output) == True

def test_check_password_prompt_with_incorrect_prompt(become_module):
    become_module.get_option.return_value = None
    b_output = to_bytes("IncorrectPrompt: ")
    assert become_module.check_password_prompt(b_output) == False
