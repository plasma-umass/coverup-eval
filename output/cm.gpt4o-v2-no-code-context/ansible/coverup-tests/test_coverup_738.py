# file: lib/ansible/plugins/filter/urls.py:26-27
# asked: {"lines": [26, 27], "branches": []}
# gained: {"lines": [26, 27], "branches": []}

import pytest
from ansible.plugins.filter.urls import do_urldecode

def test_do_urldecode(monkeypatch):
    def mock_unicode_urldecode(string):
        return "decoded_string"

    monkeypatch.setattr('ansible.plugins.filter.urls.unicode_urldecode', mock_unicode_urldecode)
    
    result = do_urldecode("encoded_string")
    assert result == "decoded_string"
