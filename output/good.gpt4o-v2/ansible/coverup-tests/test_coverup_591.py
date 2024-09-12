# file: lib/ansible/plugins/filter/urls.py:20-23
# asked: {"lines": [20, 21, 22, 23], "branches": [[21, 22], [21, 23]]}
# gained: {"lines": [20, 21, 22], "branches": [[21, 22]]}

import pytest
from ansible.module_utils.six import PY3
from ansible.module_utils.six.moves.urllib.parse import unquote_plus
from ansible.module_utils._text import to_bytes, to_text
from ansible.plugins.filter.urls import unicode_urldecode

def test_unicode_urldecode_py3(monkeypatch):
    def mock_py3():
        return True

    monkeypatch.setattr('ansible.module_utils.six.PY3', mock_py3)
    encoded_string = 'hello%20world'
    decoded_string = unicode_urldecode(encoded_string)
    assert decoded_string == 'hello world'

def test_unicode_urldecode_py2(monkeypatch):
    def mock_py3():
        return False

    monkeypatch.setattr('ansible.module_utils.six.PY3', mock_py3)
    encoded_string = 'hello%20world'
    decoded_string = unicode_urldecode(encoded_string)
    assert decoded_string == 'hello world'
