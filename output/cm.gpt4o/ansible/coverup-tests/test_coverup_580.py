# file lib/ansible/plugins/become/su.py:136-144
# lines [136, 139, 140, 142, 143, 144]
# branches []

import pytest
import re
from ansible.plugins.become import BecomeBase
from ansible.plugins.become.su import BecomeModule
from ansible.module_utils._text import to_bytes

class MockBecomeBase(BecomeBase):
    SU_PROMPT_LOCALIZATIONS = ['Password', 'Passwort']

@pytest.fixture
def become_module(mocker):
    mocker.patch('ansible.plugins.become.su.BecomeBase', MockBecomeBase)
    return BecomeModule()

def test_check_password_prompt(become_module):
    # Mock the get_option method to return None so that SU_PROMPT_LOCALIZATIONS is used
    become_module.get_option = lambda x: None

    # Test with a matching prompt
    matching_prompt = to_bytes("Password: ")
    assert become_module.check_password_prompt(matching_prompt) == True

    # Test with a non-matching prompt
    non_matching_prompt = to_bytes("NotAPasswordPrompt: ")
    assert become_module.check_password_prompt(non_matching_prompt) == False

    # Test with a localized prompt
    localized_prompt = to_bytes("Passwort: ")
    assert become_module.check_password_prompt(localized_prompt) == True

    # Test with a prompt that includes a username
    username_prompt = to_bytes("user's Password: ")
    assert become_module.check_password_prompt(username_prompt) == True

    # Test with a prompt that includes a fullwidth colon
    fullwidth_colon_prompt = to_bytes("Password：")
    assert become_module.check_password_prompt(fullwidth_colon_prompt) == True
