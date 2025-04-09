# file lib/ansible/plugins/become/su.py:94-135
# lines [94, 96, 99, 101]
# branches []

import pytest
from ansible.plugins.become import BecomeBase
from ansible.plugins.become.su import BecomeModule

@pytest.fixture
def become_su():
    return BecomeModule()

def test_become_su_localizations(become_su):
    assert become_su.name == 'su'
    assert 'Password' in become_su.SU_PROMPT_LOCALIZATIONS
    assert '口令' in become_su.SU_PROMPT_LOCALIZATIONS
    assert 'Contraseña' in become_su.SU_PROMPT_LOCALIZATIONS
    assert 'Authentication failure' in become_su.fail
