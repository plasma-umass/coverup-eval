# file lib/ansible/plugins/filter/urls.py:31-39
# lines [32, 33, 34, 36, 37, 38, 39]
# branches ['33->34', '33->36', '37->38', '37->39']

import pytest
from ansible.plugins.filter.urls import unicode_urlencode
from urllib.parse import quote, quote_plus

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Cleanup if necessary

def test_unicode_urlencode_for_qs_true_py3(mocker, cleanup):
    mocker.patch('ansible.plugins.filter.urls.PY3', True)
    result = unicode_urlencode('test value', for_qs=True)
    assert result == quote_plus('test value')

def test_unicode_urlencode_for_qs_false_py3(mocker, cleanup):
    mocker.patch('ansible.plugins.filter.urls.PY3', True)
    result = unicode_urlencode('test/value', for_qs=False)
    assert result == quote('test/value')

def test_unicode_urlencode_for_qs_true_not_py3(mocker, cleanup):
    mocker.patch('ansible.plugins.filter.urls.PY3', False)
    mocker.patch('ansible.plugins.filter.urls.to_text', side_effect=lambda x: x if isinstance(x, str) else x.decode('utf-8'))
    mocker.patch('ansible.plugins.filter.urls.to_bytes', side_effect=lambda x, encoding=None: x.encode('utf-8'))
    result = unicode_urlencode('test value', for_qs=True)
    assert result == quote_plus('test value')

def test_unicode_urlencode_for_qs_false_not_py3(mocker, cleanup):
    mocker.patch('ansible.plugins.filter.urls.PY3', False)
    mocker.patch('ansible.plugins.filter.urls.to_text', side_effect=lambda x: x if isinstance(x, str) else x.decode('utf-8'))
    mocker.patch('ansible.plugins.filter.urls.to_bytes', side_effect=lambda x, encoding=None: x.encode('utf-8'))
    result = unicode_urlencode('test/value', for_qs=False)
    assert result == quote('test/value')
