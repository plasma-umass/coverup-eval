# file httpie/sessions.py:54-57
# lines [54, 55, 56]
# branches []

import pytest
from httpie.sessions import Session
from pathlib import Path
import json

# Test function to cover the missing lines in the Session class
def test_session_class_attributes(tmp_path):
    # Create a temporary session file
    session_file = tmp_path / 'session.json'
    session_data = {
        '__meta__': {
            'httpie': '1.0.0',
            'about': 'HTTPie session file',
            'helpurl': 'https://httpie.org/doc#sessions'
        }
    }
    with session_file.open('w') as f:
        json.dump(session_data, f)

    # Load the session to trigger the missing lines
    session = Session(str(session_file))

    # Assertions to verify the session attributes
    assert session.helpurl == 'https://httpie.org/doc#sessions'
    assert session.about == 'HTTPie session file'

    # Clean up the temporary session file
    session_file.unlink()
