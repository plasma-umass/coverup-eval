# file: lib/ansible/module_utils/urls.py:658-670
# asked: {"lines": [658, 659, 662, 663, 664, 666, 670], "branches": []}
# gained: {"lines": [658, 659, 662, 663, 664, 666, 670], "branches": []}

import pytest
from ansible.module_utils.urls import ParseResultDottedDict

def test_ParseResultDottedDict_init():
    data = {'scheme': 'http', 'netloc': 'example.com'}
    result = ParseResultDottedDict(data)
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'example.com'
    assert result.__dict__ == result

def test_ParseResultDottedDict_as_list():
    data = {'scheme': 'http', 'netloc': 'example.com', 'path': '/index.html'}
    result = ParseResultDottedDict(data)
    result_list = result.as_list()
    assert result_list == ['http', 'example.com', '/index.html', None, None, None]

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: nothing to setup before each test

    yield

    # Teardown: nothing to teardown after each test
