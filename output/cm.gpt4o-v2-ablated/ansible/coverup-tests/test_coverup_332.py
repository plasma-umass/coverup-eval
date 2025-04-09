# file: lib/ansible/plugins/filter/urls.py:26-27
# asked: {"lines": [26, 27], "branches": []}
# gained: {"lines": [26, 27], "branches": []}

import pytest
from ansible.plugins.filter.urls import do_urldecode

def test_do_urldecode(monkeypatch):
    def mock_unicode_urldecode(string):
        return string[::-1]  # Mock function to reverse the string

    monkeypatch.setattr('ansible.plugins.filter.urls.unicode_urldecode', mock_unicode_urldecode)

    input_string = "test"
    expected_output = "tset"
    assert do_urldecode(input_string) == expected_output
