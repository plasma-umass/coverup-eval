# file: lib/ansible/plugins/become/su.py:136-144
# asked: {"lines": [136, 139, 140, 142, 143, 144], "branches": []}
# gained: {"lines": [136, 139, 140, 142, 143, 144], "branches": []}

import pytest
from ansible.plugins.become.su import BecomeModule
from ansible.plugins.become import BecomeBase
import re

class MockBecomeBase(BecomeBase):
    SU_PROMPT_LOCALIZATIONS = ['Password', 'Passwort', 'Mot de passe']

    def get_option(self, option):
        if option == 'prompt_l10n':
            return None
        return super().get_option(option)

@pytest.fixture
def become_module():
    return BecomeModule()

def test_check_password_prompt(become_module, mocker):
    mocker.patch.object(become_module, 'get_option', return_value=None)
    become_module.SU_PROMPT_LOCALIZATIONS = ['Password', 'Passwort', 'Mot de passe']
    
    # Test with a matching prompt
    b_output = b"Password: "
    assert become_module.check_password_prompt(b_output) == True

    # Test with a non-matching prompt
    b_output = b"Incorrect: "
    assert become_module.check_password_prompt(b_output) == False

    # Test with a localized prompt
    b_output = b"Mot de passe: "
    assert become_module.check_password_prompt(b_output) == True

    # Test with a prompt containing unicode fullwidth colon
    b_output = "Passwort：".encode('utf-8')
    assert become_module.check_password_prompt(b_output) == True
