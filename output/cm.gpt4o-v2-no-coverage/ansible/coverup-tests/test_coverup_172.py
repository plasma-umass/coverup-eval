# file: lib/ansible/galaxy/token.py:161-187
# asked: {"lines": [161, 162, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 176, 177, 178, 180, 182, 184, 185, 186, 187], "branches": [[177, 178], [177, 180]]}
# gained: {"lines": [161, 162, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 176, 177, 178, 180, 182, 184, 185, 186, 187], "branches": [[177, 178], [177, 180]]}

import pytest
import base64
from ansible.module_utils._text import to_bytes, to_text
from ansible.galaxy.token import BasicAuthToken

class TestBasicAuthToken:
    
    def test_init(self):
        token = BasicAuthToken('user', 'pass')
        assert token.username == 'user'
        assert token.password == 'pass'
        assert token._token is None

    def test_encode_token(self):
        encoded = BasicAuthToken._encode_token('user', 'pass')
        expected = to_text(base64.b64encode(to_bytes('user:pass', encoding='utf-8', errors='surrogate_or_strict')))
        assert encoded == expected

    def test_get_token_not_cached(self, mocker):
        mocker.patch.object(BasicAuthToken, '_encode_token', return_value='encoded_token')
        token = BasicAuthToken('user', 'pass')
        assert token.get() == 'encoded_token'
        assert token._token == 'encoded_token'

    def test_get_token_cached(self, mocker):
        token = BasicAuthToken('user', 'pass')
        token._token = 'cached_token'
        assert token.get() == 'cached_token'

    def test_headers(self, mocker):
        mocker.patch.object(BasicAuthToken, 'get', return_value='encoded_token')
        token = BasicAuthToken('user', 'pass')
        headers = token.headers()
        assert headers['Authorization'] == 'Basic encoded_token'
