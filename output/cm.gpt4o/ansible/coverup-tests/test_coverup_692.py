# file lib/ansible/galaxy/token.py:62-64
# lines [62, 63, 64]
# branches []

import pytest
from ansible.galaxy.token import KeycloakToken

class MockKeycloakToken(KeycloakToken):
    def __init__(self, client_id, access_token):
        self.client_id = client_id
        self.access_token = access_token

def test_form_payload():
    client_id = 'test_client_id'
    access_token = 'test_access_token'
    token = MockKeycloakToken(client_id, access_token)
    
    expected_payload = 'grant_type=refresh_token&client_id=test_client_id&refresh_token=test_access_token'
    actual_payload = token._form_payload()
    
    assert actual_payload == expected_payload

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
