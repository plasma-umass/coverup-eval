# file httpie/sessions.py:54-57
# lines [54, 55, 56]
# branches []

import pytest
from httpie.sessions import Session

def test_session_class_attributes():
    # Verify that the class attributes are set correctly
    assert Session.helpurl == 'https://httpie.org/doc#sessions'
    assert Session.about == 'HTTPie session file'
