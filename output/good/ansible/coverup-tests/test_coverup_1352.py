# file lib/ansible/plugins/become/su.py:136-144
# lines [139, 140, 142, 143, 144]
# branches []

import pytest
from ansible.plugins.become import su

@pytest.fixture
def su_plugin(mocker):
    mocker.patch.object(su.BecomeModule, '_build_success_command', return_value=b'')
    return su.BecomeModule()

def test_check_password_prompt_with_localization(su_plugin):
    # Mock the get_option to return None to trigger the default SU_PROMPT_LOCALIZATIONS
    su_plugin.get_option = lambda x: None if x == 'prompt_l10n' else su_plugin._get_option(x)
    
    # Test with a localized prompt
    localized_prompt = b"Password:"
    assert su_plugin.check_password_prompt(localized_prompt) == True

    # Test with a different localized prompt
    localized_prompt = b"password for user:"
    assert su_plugin.check_password_prompt(localized_prompt) == True

    # Test with a prompt not in the localizations
    not_localized_prompt = b"Enter passphrase:"
    assert su_plugin.check_password_prompt(not_localized_prompt) == False

    # Cleanup is handled by the fixture scope
