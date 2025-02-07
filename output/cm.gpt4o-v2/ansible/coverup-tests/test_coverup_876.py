# file: lib/ansible/plugins/filter/urls.py:26-27
# asked: {"lines": [26, 27], "branches": []}
# gained: {"lines": [26, 27], "branches": []}

import pytest
from ansible.plugins.filter.urls import do_urldecode
from ansible.module_utils.six import PY3

def test_do_urldecode_py3(monkeypatch):
    if not PY3:
        monkeypatch.setattr('ansible.module_utils.six.PY3', True)
    decoded_string = do_urldecode('hello%20world')
    assert decoded_string == 'hello world'

def test_do_urldecode_py2(monkeypatch):
    if PY3:
        monkeypatch.setattr('ansible.module_utils.six.PY3', False)
    decoded_string = do_urldecode('hello%20world')
    assert decoded_string == 'hello world'
